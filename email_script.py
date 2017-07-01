#!/usr/bin/env python

import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from parse import process_message, process_receipients, process_arguments
from server import connect_to_server, login_to_server

'''
This is a script to send emails from python using the email
thetatau.media@gmail.com

This can be extended to other emails, if not hardcoded
'''

exception_string = """\
Usage: ./email_script.py <subject> <message> <message file>
Use -h to show help"""

opts, args = process_arguments()
try:
    if len(args) < 2:
        raise Exception(exception_string)
except Exception as e:
    print(e)
    sys.exit()

subject = args[0]
text_file = process_message(args[1])
print('Connecting to mail server...')
server = connect_to_server()
logged_in, email = login_to_server(server)
if logged_in:
    receipients = process_receipients(sys.argv[1])

server.quit()

greetings = ['Hey', 'Hello', 'What\'s up']


def send_message(server, email, receipient, subject, message):
    # TODO add greeting selection
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = email
        msg['To'] = receipient

        text = message['text']
        html = message['html']

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        msg.attach(part1)
        msg.attach(part2)

        server.sendmail(email, receipient, msg.as_string())
    except:
        print('Error while sending email to {}'.format(receipient))


print('Connecting to server...\n')
server = connect_to_server()
logged_in, email = login_to_server(server)
