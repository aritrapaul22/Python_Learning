import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email settings
sender_email = "aritra.paul@rediffmail.com"
receiver_email = "ifjlrtqqh@emlhub.com"
subject = "Test Email"
body = "This is a test email sent from a Python script."
password = "Amirediffe@2"  # Use your actual Rediffmail password

# Set up the MIME
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to the message
message.attach(MIMEText(body, "plain"))

# SMTP server settings for Rediffmail
smtp_server = "smtp.rediffmail.com"
port = 587  # TLS port for Rediffmail
# port = 465  # For SSL
server = None

try:
    # Create an SMTP connection and start TLS
    server = smtplib.SMTP(smtp_server, port, timeout=10)
    server.ehlo()  # Identify yourself to the server
    server.starttls()  # Start TLS encryption
    server.ehlo()  # Re-identify after TLS encryption

    # Login to the server
    server.login(sender_email, password)

    # Send the email
    print("Logging in...")
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")

except smtplib.SMTPException as smtp_error:
    print(f"SMTP error occurred: {smtp_error}")
except Exception as e:
    print(f"General error occurred: {e}")

finally:
    # Quit the server if the connection was established
    if server:
        try:
            server.quit()
        except Exception as quit_error:
            print(f"Failed to quit the server properly: {quit_error}")
