# Manual Log Analysis — Compromised WordPress

### 📘 Overview
This project demonstrates a **manual log analysis** of a compromised WordPress web server.  
All analysis was performed **without using a SIEM or specialized tools**. I've only used basic **Linux commands** such as `grep`, `cut`, `sort`, and `uniq`.

The goal was to build confidence with command-line log analysis by extracting indicators (IP, path, filename) and creating a short timeline of events.

![giphy (6)](https://github.com/user-attachments/assets/8deb28e1-70cf-4694-a1e0-8f9efd0fd16b)

---

### 🧩 Scenario
The log file used in this project comes from a **Blue Team Labs Online** challenge:  
**[Compromised WordPress](https://blueteamlabs.online/home/challenge/log-analysis-compromised-wordpress-ce000f5b59)**

In the scenario, an attacker exploited a vulnerable WordPress plugin to **upload a malicious file** disguised as an image, then **executed it remotely** to gain control of the server.

---

### 🎯 Objective
1. Perform manual log analysis without SIEM tools.  
2. Identify suspicious patterns in HTTP requests.  
3. Extract Indicators of Compromise (IOCs) such as IP addresses, upload paths, and filenames.  
4. Summarize findings in a short investigation report (`Investigation Report.pdf`).

---

### 🧠 Key Findings

- Vulnerable WordPress plugin allowed arbitrary file uploads.
- Attacker uploaded fr34k.png, which later appeared as fr34k.php.
- Malicious activity observed from multiple IPs, mostly from foreign networks.
- Requests suggest webshell interaction after upload.
- The investigation confirmed full compromise of the WordPress instance.

---

### 📄 Report

The final findings are summarized in:
````reports/Investigation Report.pdf````

It includes:
- Timeline of the compromise
- Suspicious IPs
- Vulnerable components
- Recommended mitigations

