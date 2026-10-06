# NOWHERE Port Scanner

This is a simple port scanner I made in Python.

The project started from a tutorial by **CyberFlows Academy**, where we built a basic port scanner. After finishing the tutorial I wanted to play around with the code and see if I could improve it and add some more features myself.

## What it does

The scanner checks TCP ports on an IP address or domain and shows which ports it can connect to.

It currently has three scan options:

* **Quick scan** – ports 1-1024
* **Full scan** – ports 1-65535
* **Custom scan** – choose the port range yourself

For open ports it also tries to find the service running on the port and grab a banner/version if the service returns one.

Example output:

```text
PORT    PROTOCOL  SERVICE        VERSION
-----------------------------------------
22      tcp       ssh            SSH-2.0-OpenSSH_9.6
80      tcp       http           nginx/1.18.0
443     tcp       https
```

## What I changed

The original scanner from the tutorial was pretty simple. It scanned ports 1-499 one at a time and printed the open ports and banners it found.

I wanted to see if I could build a bit more on top of it, so I added:

* Multithreading with `ThreadPoolExecutor`
* Quick, full and custom port scans
* Service detection with `socket.getservbyport()`
* Better banner grabbing
* An HTTP request for services that don't send a banner automatically
* Cleaner output
* Error handling for targets that can't be resolved
* A small menu for choosing the scan type
* NOWHERE ASCII banner because why not :)

One of the biggest changes was multithreading. The original version checked one port at a time, which became really slow when scanning a lot of ports. Using threads lets the scanner check multiple ports at the same time.

## Installation

Clone the repository and install IPy:

```bash
pip install IPy
```

Then run:

```bash
python portscanner.py
```

Enter an IP address or domain when prompted:

```text
[+] Enter Target To Scan: 192.168.1.10

[+] Choose scan type:
    1) Quick   (ports 1-1024)
    2) Full    (ports 1-65535)
    3) Custom  (choose your own range)
```

There are still things I want to improve and experiment with, so this is very much a learning project.

## Credits

The starting point for this project was a port scanner tutorial from **CyberFlows Academy**. I used the scanner from the tutorial as the base and then changed and expanded it as part of my own Python practice.

## Disclaimer

For educational use and authorized testing only. Only scan systems you own or have permission to test.
