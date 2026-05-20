# "Assalam Walaikum Bhaia. Please check the code below and appreciate any suggestion for improvising"

import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load credentials securely from environment variables
login = os.environ.get('EMAIL_USER')
password = os.environ.get('EMAIL_PASS')

# Email parameters
from_address = login
to_address = 'mashihoor@gmail.com'
subject = 'Email Using Python'
body = 'Assalam Walaikum bhaia. Please check the coding and appreciate your feedback. - Rezwan.'

# Use a relative path so it works seamlessly on GitHub or any machine
filename = 'EmailByPython_Rezwan3.py' 

# SMTP server details (for example, for Gmail)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Create the multipart container
msg = MIMEMultipart()
msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = subject

# Attach the body with the msg instance
msg.attach(MIMEText(body, 'plain'))

# Attach the file
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename={filename}')
    msg.attach(part)

# Connect to the server
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()  # Secure the connection
server.login(login, password)  # Login to the email account

# Send the email
server.sendmail(from_address, to_address, msg.as_string())

# Disconnect from the server
server.quit()