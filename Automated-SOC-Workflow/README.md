# 🧠 Automated SOC Workflow (Splunk x n8n x AI x Slack)

This project demonstrates how to build an **automated SOC workflow** that detects, enriches, and reports security alerts using a combination of **Splunk**, **n8n**, **AI**, and **Slack**.

---

### ⚙️ Overview

The goal of this project was to automate the process of analyzing and reporting security events.  
When a suspicious activity (for example, a brute-force attempt) is detected in **Splunk**, it triggers an **n8n workflow** that:

1. Receives the alert via **Webhook**
2. **Enriches** the IOC (IP address) using **AbuseIPDB**
3. **Summarizes** the findings with an **AI model**
4. Sends a formatted report directly to **Slack**

---

### 🧩 Workflow Structure
Splunk → Webhook (n8n) → AI Message Node → AbuseIPDB Enrichment → Slack Message


### 🧰 Tools Used
| Tool / Service | Purpose |
|----------------|----------|
| **Splunk** | Security event detection and alerting |
| **n8n** | Automation platform for workflows |
| **OpenAI Model** | Summarizes and explains alerts |
| **AbuseIPDB API** | OSINT enrichment for IP addresses |
| **Slack** | Delivery of formatted SOC alerts |

---

### 📡 Example Workflow
<img width="1128" height="545" alt="n8n_workflow" src="https://github.com/user-attachments/assets/ad190672-b0da-443a-8545-a4478bacae5b" />


The workflow listens for Splunk alerts, enriches IOC data, and automatically posts a security summary into Slack.

---

### 💬 Example Slack Output
<img width="1418" height="589" alt="slack_message" src="https://github.com/user-attachments/assets/bd7c8e9d-08f3-4e78-9a9b-781655afc45d" />

**Alert Summary:**
> The alert “Test-Brute-Force” was triggered involving suspicious login attempts on `DESKTOP-S7LALCD`.  
> AI summarization and IOC enrichment were performed automatically, identifying the IP, ISP, and threat score from AbuseIPDB.

---

### 🧠 Key Learning Points
- Automating SOC processes with **n8n**
- Integrating **Splunk** alerts via Webhooks
- Using **OSINT APIs** for enrichment
- Generating AI-based **incident summaries**
- Sending real-time **Slack notifications**

---

### 🚀 Future Improvements
- Add VirusTotal and Shodan lookups for deeper enrichment  
- Include automatic ticket creation (e.g. Jira or TheHive)  
- Enhance AI summarization with confidence scoring  


