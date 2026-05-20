# Secure Python SMTP Email Automation

## Description
A Python-based automation script designed to programmatically send emails with attachments. This project demonstrates secure application integration by authenticating via Google App Passwords—a dedicated, 16-character application-specific credential—allowing the script to execute successfully without exposing the primary user account password.

## Key Accomplishments
* **Automated Delivery:** Configured programmatic email and attachment routing using Python's `smtplib` protocol.
* **Secure Authentication:** Utilized application-specific passwords to grant the script restricted, application-level access to the Google SMTP server.
* **Credential Management:** Demonstrated security best practices by decoupling the primary account password from the automated workflow, minimizing the risk of broader account compromise.

## Execution
The script successfully executes via the command line, assembling a multipart MIME message, encoding a file attachment in base64, and delivering it to the target inbox.
