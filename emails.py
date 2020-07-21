import smtplib

SENDER_EMAIl = 'pratiksharma8@gmail.com'
SENDER_PASSWORD = 'Patrick@510'


def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIl, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIl, receiver_email, message)


send_email('ghimiresurakshya@gmail.com', 'AHAHAHAHAH', 'She is so cute.. AHAAHHAHAHAHA')
