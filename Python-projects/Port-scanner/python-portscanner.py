import shutil
import socket
from IPy import IP
from concurrent.futures import ThreadPoolExecutor

VERSION = "1.0#dev"

# the ascii name that gets printed at the start
WORDMARK = [
    '    _   ______ _       ____  ____________  ______',
    '   / | / / __ \\ |     / / / / / ____/ __ \\/ ____/',
    '  /  |/ / / / / | /| / / /_/ / __/ / /_/ / __/   ',
    ' / /|  / /_/ /| |/ |/ / __  / /___/ _, _/ /___   ',
    '/_/ |_/\\____/ |__/|__/_/ /_/_____/_/ |_/_____/   ',
]

# colors for the terminal (ANSI codes)
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def print_banner():
    # check how wide the terminal is so the name doesnt get messed up
    term_width = shutil.get_terminal_size().columns
    word_width = max(len(line) for line in WORDMARK)

    print()
    if term_width >= word_width:
        for line in WORDMARK:
            print(f"{CYAN}{BOLD}{line}{RESET}")
        print()
        print(f"{DIM}Port Scanner  {{{VERSION}}}{RESET}")
        print(f"{DIM}Only scan what you own or have permission to test.{RESET}")
    else:
        # terminal is too small for the big name
        print(f"{CYAN}{BOLD}NOWHERE{RESET} Port Scanner {{{VERSION}}}")
    print()


def check_ip(ip):
    # if its already an ip we just use it
    try:
        IP(ip)
        return ip
    # if not its probably a domain name, so look up the ip
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(sock):
    # tries to read what the service says when we connect (the version etc)
    sock.settimeout(1.0)

    # some services like ssh and ftp say hi by themselves
    try:
        data = sock.recv(1024)
    except socket.timeout:
        data = b''

    # others (like http) only answer if we send something first
    if not data:
        try:
            sock.sendall(b'HEAD / HTTP/1.0\r\n\r\n')
            data = sock.recv(1024)
        except OSError:
            return ''

    # turn the bytes into normal text
    text = data.decode(errors='ignore').strip()
    if not text:
        return ''

    # for http we only want the server line, like nginx/1.18.0
    for line in text.splitlines():
        if line.lower().startswith('server:'):
            return line.split(':', 1)[1].strip()

    # otherwise just use the first line, cut it so its not too long
    return text.splitlines()[0][:60]


def scan_port(ipaddress, port):
    # tries to connect to one port, returns info if its open
    try:
        with socket.socket() as sock:
            sock.settimeout(0.5)
            sock.connect((ipaddress, port))

            # find the name of the service, like 80 = http
            try:
                service = socket.getservbyport(port)
            except OSError:
                service = 'unknown'

            # try to get the version
            try:
                banner = get_banner(sock)
            except OSError:
                banner = ''

            return (port, 'tcp', service, banner)
    except (socket.timeout, ConnectionRefusedError, OSError):
        # couldnt connect so the port is closed (or filtered)
        return None


def scan(target, start=1, end=1025):
    # make sure we have an ip, stop if the domain doesnt exist
    try:
        converted_ip = check_ip(target)
    except socket.gaierror:
        print(f'[-] Could not resolve target: {target}')
        return

    print(f'\n[Scanning Target] {target}\n')
    print(f'{"PORT":<8}{"PROTOCOL":<10}{"SERVICE":<15}VERSION')
    print('-' * 41)

    found = 0
    # threads let us scan a lot of ports at the same time, much faster
    with ThreadPoolExecutor(max_workers=300) as executor:
        # map keeps the results in the same order as the ports
        results = executor.map(lambda p: scan_port(converted_ip, p), range(start, end))

        for result in results:
            # None means the port was closed so we skip it
            if result:
                port, protocol, service, banner = result
                print(f'{port:<8}{protocol:<10}{service:<15}{banner}')
                found += 1


    print(f'\n{found} open port(s) found\n')


def choose_ports():
    # lets the user pick how many ports to scan
    print('[+] Choose scan type:')
    print('    1) Quick   (ports 1-1024)')
    print('    2) Full    (ports 1-65535)')
    print('    3) Custom  (choose your own range)')
    choice = input('[+] Choice (1/2/3): ').strip()

    if choice == '2':
        return 1, 65536

    if choice == '3':
        try:
            start = int(input('    Start port: '))
            end = int(input('    End port: '))
            # ports only go from 1 to 65535
            if 1 <= start <= end <= 65535:
                # +1 because range() stops before the last number
                return start, end + 1
        except ValueError:
            # user typed something that isnt a number
            pass
        print('[-] Invalid range, using quick scan instead.')

    # quick scan is the default
    return 1, 1025


if __name__ == "__main__":
    print_banner()
    target = input('[+] Enter Target To Scan: ').strip()
    start, end = choose_ports()
    scan(target, start, end)