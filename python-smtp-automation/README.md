# Secure Python SMTP Email Automation

## Objective
A Python-based automation script utilizing the `smtplib` and `email.mime` libraries to programmatically send emails with attachments. 

## Skills Demonstrated
* **Python Scripting:** Automated routine communication tasks.
* **Protocol Handling:** Established secure TLS connections via SMTP over port 587.
* **Credential Security:** Implemented environment variables (`os.environ`) to ensure App Passwords and credentials remain decoupled from the source code.

## Execution
The script successfully executes via the command line, assembling a multipart MIME message, encoding a file attachment in base64, and delivering it to the target inbox.
