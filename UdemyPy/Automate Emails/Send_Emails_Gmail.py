import yagmail, os, pandas


def simple_email(sender):
    receiver = 'randomemails@mail.tk'
    subject = "This is the subject."
    contents = """
    Hi,
    Here is the content of the email.
    Thanks!
    """

    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")


def send_email_multiple_address(sender):
    subject = "This is the subject."

    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

    df = pandas.read_csv('contacts.csv')

    for index, row in df.iterrows():
        contents = f"""
        Hi {row['name']},
        
        Here is the content of the email.
        Thanks!
        """
        yag.send(to=row['email'], subject=subject, contents=contents)
        print("Email Sent!")


def send_email_with_attachment(sender):
    receiver = 'randomemails@mail.tk'
    subject = "This is the subject."
    contents = ["""
        Hi,
        Here is the content of the email.
        Thanks!
        """, 'text.txt']

    yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")

def main():
    sender = 'aritra.paul22@gmail.com'
    simple_email(sender)
    send_email_multiple_address(sender)
    send_email_with_attachment(sender)


if __name__ == '__main__':
    main()
