# AWS Cloud SIEM Deployment & Telemetry Analysis Lab

## 📌 Project Overview
This project demonstrates the deployment of a centralized **Wazuh SIEM Manager** within an AWS cloud architecture to monitor real-time security telemetry from a remote Linux endpoint (**Wazuh Agent**). The core objective of this lab was to establish a secure telemetry pipeline, optimize log ingestion via global logging configurations, and observe authentication data flows under simulated brute-force events.

---

## 🏗️ System Architecture
* **Security Event Collector:** Wazuh Manager & Dashboard (Ubuntu EC2 Instance)
* **Monitored Endpoint:** Ubuntu Server Agent (EC2 Instance)
* **Infrastructure Security:** AWS Stateful Security Groups restricting traffic to required ports (SSH Port 22, Wazuh Agent ports 1514/1515 TCP).

---

## 🛠️ Phases & Skills Demonstrated

### 1. Cloud Infrastructure & Security Group Engineering
* Provisioned cloud computing environments within AWS EC2.
* Architected perimeter defense rules via AWS Security Groups to allow strict management access and prevent unrestricted public exposure to sensitive ports.

### 2. SIEM Configuration & Pipeline Engineering
* Interacted with Linux server architecture utilizing terminal-based text editors (`nano`).
* Configured advanced XML tracking parameters within the core initialization script (`/var/ossec/etc/ossec.conf`).
* Successfully transitioned the SIEM platform from standard threshold alerting to absolute data retention by enabling `<logall>yes</logall>` and `<logall_json>yes</logall_json>`.

### 3. Log Diagnostics & Telemetry Validation
* Resolved common operational friction points including relative vs. absolute file path directory constraints and networking connection timeouts.
* Utilized native Linux log-streaming utilities (`tail -f`, `grep`) to analyze raw system event feeds in real time.
* Verified proper handshake mechanics between remote agents and the central analysis manager.

## 📊 Project Artifacts & Results

### 🟢 Ingestion Phase: Successful Agent Connection
The screenshot below confirms that the remote Ubuntu endpoint successfully registered and established an active handshake with the central cloud-based Wazuh Manager:

<img width="1912" height="870" alt="Screenshot 2026-05-13 164658" src="https://github.com/user-attachments/assets/a61d492d-521f-4fd5-9368-04375056b192" />

### ⚙️ Engineering Phase: Activating Global Archive Logging
To transition the SIEM platform from standard threshold-based alerting to absolute data retention, the central manager's core initialization script (`/var/ossec/etc/ossec.conf`) was modified using terminal-based text editors. 

By altering the global configuration block, the system was engineered to archive all incoming events into JSON formats for deep forensic analysis:

```xml
<ossec_config>
  <global>
    <jsonout_output>yes</jsonout_output>
    <alerts_log>yes</alerts_log>
    <logall>yes</logall>
    <logall_json>yes</logall_json>
  </global>
</ossec_config>
