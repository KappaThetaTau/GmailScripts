import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

greetings = ['Hey', 'Hello', 'What\'s up']


def create_message(email, receipient, subject, message):
    name = receipient['name']
    greeting = greetings[random.randrange(len(greetings))]
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = "Theta Tau - Historians"
    msg['To'] = '{0} {1}'.format(name['first'], name['last'])

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
        msg = create_message(email, receipient, subject, message)
        server.sendmail(email, receipient['email'], msg.as_string())
    except Exception as e:
        print('Error while sending email to {}'.format(receipient))
        print(e)
