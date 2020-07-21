import smtplib

SENDER_EMAIl = 'YOUR EMAIL'
SENDER_PASSWORD = 'YOUR PASSWORD'


def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIl, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIl, receiver_email, message)


send_email('RECEIVER EMAIL', 'SUBJECT', 'BODY')
