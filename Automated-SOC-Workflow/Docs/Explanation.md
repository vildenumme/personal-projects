# Explanation

### Workflow Summary
This workflow connects Splunk with n8n to automate SOC alerts.

1. **Splunk Alert**
   - Detects suspicious activity (e.g. brute-force attempts)
   - Sends alert via Webhook to n8n

2. **n8n Workflow**
   - Receives the alert (Webhook node)
   - Extracts IOC (IP address)
   - Looks up IP in **AbuseIPDB** for threat intelligence
   - Sends alert details to **AI model** for summarization
   - Posts the enriched and summarized message to **Slack**

3. **Slack Notification**
   - Displays all relevant details (IOC, risk, recommended actions)

### Example Use Case
- Splunk detects 10 failed logins → workflow enriches and sends alert in <10 seconds.

