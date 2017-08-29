import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

greetings = ['Hey', 'Hello', 'What\'s up']


def create_message(receipient, subject, message):
    """
    Creates a message to be emailed,
    formats if replacement strings included in the message

    Currently supported replacement strings include

    * $name - replaced by name from csv
    * $greeting - randomly chosen greeting from 'greetings' array

    Parameters
    ----------
    receipient : dict
        Contains receipient information, specifically

        + name
        + email

    subject : string
        The subject of the email

    message : dict
        Contains the message in both plaintext and html format

    Returns
    -------
    msg : email.mime.multipart.MIMEMultipart
        email message to be sent
    """
    name = receipient['name']
    greeting = greetings[random.randrange(len(greetings))]
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = "Theta Tau - Rush Chair"
    msg['To'] = receipient['email']

    html = message['html'].replace(
            '$name', name['first']).replace(
                    '$greeting', greeting)
    text = message['text'].replace(
            '$name', name['first']).replace(
                    '$greeting', greeting)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    return msg


def send_message(server, email, receipient, subject, message):
    try:
        msg = create_message(receipient, subject, message)
        server.sendmail(email, receipient['email'], msg.as_string())
    except Exception as e:
        print('Error while sending email to {}'.format(receipient))
        print(e)
