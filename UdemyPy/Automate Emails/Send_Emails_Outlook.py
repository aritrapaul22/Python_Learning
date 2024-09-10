import smtplib, os
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders

from adodbapi.examples.xls_read import filename


def send_from_outlook():
    sender = 'aritra.paul@outlook.in'
    receiver = 'rando_email@gmail.com'
    password = 'pythonpass1234'

    message = """\
    Subject: Hello Hello
    
    This is Aritra!
    Just wanted to say hi!
    """

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    server.quit()


def send_rich_html_email():
    sender = 'aritra.paul@outlook.in'
    receiver = 'rando_email@gmail.com'
    password = 'pythonpass1234'

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Hello Again!'

    body = """
    <h1>Hi There</h1>
    Here is the rich content.
    """

    mimetext = MIMEText(body, 'html')
    message.attach(mimetext)

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, password)
    message_text = message.as_string()
    server.sendmail(sender, receiver, message_text)
    server.quit()


def send_rich_email_with_attachment():
    sender = 'aritra.paul@outlook.in'
    receiver = 'rando_email@gmail.com'
    password = 'pythonpass1234'

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = 'Hello Again!'

    body = """
        <h1>Hi There</h1>
        Here is the rich content.
        """

    mimetext = MIMEText(body, 'html')
    message.attach(mimetext)

    attachement_path = 'tiger.jpg'
    attachment_file = open(attachement_path, 'rb')
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload(attachment_file.read())
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=attachement_path)
    message.attach(payload)


    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(sender, password)
    message_text = message.as_string()
    server.sendmail(sender, receiver, message_text)
    server.quit()

if __name__ == '__main__':
    send_from_outlook()
    send_rich_html_email()
    send_rich_email_with_attachment()
