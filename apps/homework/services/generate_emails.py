from faker import Faker

def generate_email(amount:int=20):
    fake = Faker()

    for _ in range(amount):
        email = fake.email()
        yield email


def read_emails():
    emails = []
    for email in generate_email():
        email_to_show = f"<li>{email}</li>"
        emails.append(email_to_show)
    result = ''.join(emails)
    return result

def show_emails():
    return read_emails()

