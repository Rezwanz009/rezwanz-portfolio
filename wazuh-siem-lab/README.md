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
This snapshot displays the core server configuration file (`ossec.conf`) demonstrating the transition from standard high-threshold alerting to full data retention:

[DRAG_AND_DROP_TERMINAL_CONFIG_HERE]

### 🚨 Threat Ingestion Phase: Real-Time SSH Telemetry Ingestion
This artifact captures the live Wazuh Dashboard processing authentication logs generated during the simulated brute-force events:

[DRAG_AND_DROP_ALERTS_HERE]
---

## 📊 Project Artifacts & Results
*(Pro-tip: Once your repo is created, you can drag and drop your screenshots right here into the editor to show off your active Wazuh Agent dashboard donut chart!)*
