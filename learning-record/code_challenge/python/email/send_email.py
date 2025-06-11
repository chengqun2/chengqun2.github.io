import smtplib
from email.mime.text import MIMEText

# Email content
subject = "Test Email"
body = "This is a test email sent via Postfix using Python."
sender_email = "root@ycjjapp"
recipient_email = "chengqun710@163.com"

# Create MIMEText object
msg = MIMEText(body)
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email

# Send the email via local Postfix server
with smtplib.SMTP("36.152.142.226", 25) as server:
    server.sendmail(sender_email, [recipient_email], msg.as_string())
