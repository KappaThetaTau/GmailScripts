#!/usr/bin/env python

import sys
import getpass
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

'''
This is a script to send emails from python using the email
thetatau.media@gmail.com

This can be extended to other emails, if not hardcoded
'''

try:
    if len(sys.argv) < 4:
        raise Exception("""Usage: ./email_script.py <email csv>
                        <subject> <message file> \nPlease read
                        the README for more information""")
except Exception as e:
    print(e)
    sys.exit()

greetings = ['Hey', 'Hello', 'What\'s up']


def connect_to_server():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    return server


def get_credentials():
    # for other emails, use input('Which email would you like to use?')
    email = 'thetatau.media@gmail.com'
    password = getpass.getpass(
            'Please input the password to {}: '.format(email))
    return {'email': email, 'password': password}


def login_to_server(server):
    authenticated = False
    for i in range(3):
        try:
            credentials = get_credentials()
            print('Authenticating...\n')
            server.login(credentials['email'], credentials['password'])
        except Exception as e:
            print(e)
            print('Please try again')
        else:
            authenticated = True
            break
    return (authenticated, credentials['email'])


def process_message(message_file):
    message = ""
    try:
        with open(message_file) as f:
            message = f.read()
        f.close()
    except Exception as e:
        print(e)
        sys.exit()
    message = message.replace('\n', ' ').replace('\r', ' ')
    return message


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


def process_receipients(receipients_csv):
    receipients = []
    with open(receipients_csv) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            first_name = row[0].split(' ', 1)[0]
            receipient = {'name': first_name, 'email': row[1]}
            receipients.append(receipient)
    f.close()
    return receipients

print('Connecting to server...\n')
server = connect_to_server()
logged_in, email = login_to_server(server)

if logged_in:
    message = process_message(sys.argv[3])
    receipients = process_receipients(sys.argv[1])
    for receipient in receipients:
        send_message(email, receipient, subject, message)
server.quit()
