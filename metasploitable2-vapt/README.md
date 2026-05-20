# Metasploitable 2 Vulnerability Assessment and Penetration Test (VAPT)

## Executive Summary
This project documents a comprehensive Vulnerability Assessment and Penetration Testing (VAPT) engagement conducted against a Metasploitable2 target system. The primary objective was to identify security vulnerabilities and demonstrate the potential impact of successful exploitation.

## Tools Used
* **Nmap:** Network scanning and service detection.
* **Metasploit Framework:** Exploitation and post-exploitation activities.
* **MySQL Client:** Database connection and enumeration.

## Methodology

### 1. Reconnaissance
The engagement began with identifying the attacker and target IP addresses on the local network. 
* **Attacker Machine (Kali Linux):** Identified as `192.168.245.132` via `ifconfig`.
![Kali Linux IP](<images/Linux IP.png>)

* **Target Machine (Metasploitable 2):** Discovered at `192.168.245.133` using an ARP scan.
![Target IP Discovery](<images/Metasploitable 2 IP.png>)

### 2. Vulnerability Scanning
An aggressive Nmap service scan (`nmap -sV`) was executed against the target IP to identify open ports, running services, and specific software versions. 

**Nmap Scan Snippet:**
![Nmap Scan Part 1](<images/01 2024-07-18 124828.png>)
![Nmap Scan Part 2](<images/02 2024-07-18 124935.png>)

*(Note: The full 900+ line Nmap outputs detailing FTP, SSH, SMTP, HTTP, RPC, NetBIOS, MySQL, PostgreSQL, and VNC services are available in the `exploitation-logs` directory).*

### 3. Exploitation & Key Findings
The assessment revealed an overall risk to the target system of **CRITICAL**. Six critical services were successfully exploited:
* **FTP (Port 21):** Exploited a vsftpd 2.3.4 Backdoor to achieve root access and the ability to execute arbitrary commands.
* **SSH (Port 22):** Gained user-level access via a brute-force attack on weak credentials (username "user" and password "user").
* **SMTP (Port 25):** Successfully enumerated valid system users to gather information for further attacks.
* **HTTP (Port 80):** Leveraged a PHP CGI Argument Injection (CVE-2012-1823) to gain a Meterpreter session and execute arbitrary PHP code.
* **MySQL (Port 3306):** Authenticated as the root user by exploiting an empty password, gaining the ability to view and modify all databases.
* **VNC (Port 5900):** Achieved full graphical access by performing a password guessing attack and exploiting a weak password ("password").

## Detailed Exploitation Logs
For a deeper technical dive, full command-line outputs and exploitation evidence for each service are documented in the `/exploitation-logs` directory of this repository.

## Recommendations
Immediate action is recommended to address these vulnerabilities and improve the overall security posture of the system. Key recommendations include upgrading vsftpd and Apache/PHP to the latest stable versions, implementing strong password policies for SSH, VNC, and MySQL, and configuring the SMTP server to prevent user enumeration.
