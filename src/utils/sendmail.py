import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

greetings = ['Hey', 'Hello', 'What\'s up']


def personalize(template, first_name, greeting):
    """
    Fills the replacement strings in a message template

    Currently supported replacement strings include

    * $name - replaced by name from csv
    * $greeting - greeting from the 'greetings' array

    If no name is available, '$name' is removed (along with the
    space before it) so greetings like '$greeting $name,' still
    read naturally

    Parameters
    ----------
    template : string
        Message template, in plaintext or html

    first_name : string
        First name of the receipient, may be empty

    greeting : string
        Greeting to fill in for '$greeting'

    Returns
    -------
    message : string
        Template with the replacement strings filled in
    """
    if first_name:
        message = template.replace('$name', first_name)
    else:
        message = template.replace(' $name', '').replace('$name', '')
    return message.replace('$greeting', greeting)


def create_message(receipient, sender, from_name, subject, message):
    """
    Creates a message to be emailed,
    formats if replacement strings included in the message
    (see personalize)

    Parameters
    ----------
    receipient : dict
        Contains receipient information, specifically

        + name
        + email

    sender : string
        Email address the message is sent from

    from_name : string
        Display name shown alongside the sender address

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
    msg['From'] = '{} <{}>'.format(from_name, sender)
    msg['To'] = receipient['email']

    html = personalize(message['html'], name['first'], greeting)
    text = personalize(message['text'], name['first'], greeting)

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)
    return msg


def send_message(server, email, receipient, subject, message, from_name):
    """
    Sends one personalized message,
    printing errors instead of raising

    Parameters
    ----------
    server : smtplib.SMTP_SSL
        Authenticated server to send from

    email : string
        Email address the message is sent from

    receipient : dict
        Contains receipient information, specifically

        + name
        + email

    subject : string
        The subject of the email

    message : dict
        Contains the message in both plaintext and html format

    from_name : string
        Display name shown alongside the sender address

    Returns
    -------
    sent : bool
        True if the message was accepted by the server
    """
    try:
        msg = create_message(receipient, email, from_name, subject, message)
        server.sendmail(email, receipient['email'], msg.as_string())
    except Exception as e:
        print('Error while sending email to {}'.format(receipient['email']))
        print(e)
        return False
    return True
