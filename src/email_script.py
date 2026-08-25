#!/usr/bin/env python

import sys
import time
from utils import parse, server, sendmail

'''
This is a script to send emails from python
'''

exception_string = """\
Usage: ./email_script.py <plaintext_file> <html_file> [options]
Use -h to show help"""

opts, args = parse.process_arguments()
try:
    if len(args) < 2:
        raise Exception(exception_string)
except Exception as e:
    print(e)
    sys.exit()

opts = vars(opts)
subject = input('What would you like the subject of the email to be?\n')
text_file = parse.process_message(args[0])
html_file = parse.process_message(args[1])
message = {'text': text_file, 'html': html_file}

receipients = parse.process_receipients(opts['email_csv'])
if len(receipients) == 0:
    print('No recipients found in {}'.format(opts['email_csv']))
    sys.exit()

preview = sendmail.personalize(
        message['text'], receipients[0]['name']['first'],
        sendmail.greetings[0])
print('\nPreview (plaintext version, as sent to {}):'.format(
        receipients[0]['email']))
print('-' * 40)
print('From: {}'.format(opts['from_name']))
print('Subject: {}'.format(subject))
print()
print(preview)
print('-' * 40)

confirm = input('Send to {} recipient(s)? (y/N) '.format(len(receipients)))
if confirm.strip().lower() not in ('y', 'yes'):
    print('Aborted, no email was sent')
    sys.exit()

print('Connecting to mail server...')
mail_server = server.connect_to_server()
logged_in, email = server.login_to_server(mail_server)

if logged_in:
    print('Successfully authenticated, sending mail...')
    failures = []
    total = len(receipients)
    for i, receipient in enumerate(receipients, start=1):
        sent = sendmail.send_message(
                mail_server, email, receipient, subject, message,
                opts['from_name'])
        if sent:
            print('[{}/{}] Sent to {}'.format(i, total, receipient['email']))
        else:
            failures.append(receipient['email'])
        if i < total and opts['delay'] > 0:
            time.sleep(opts['delay'])
    print('Finished: {} sent, {} failed'.format(
            total - len(failures), len(failures)))
    if failures:
        print('Failed recipients:')
        for address in failures:
            print('  ' + address)
print('Exiting')

mail_server.quit()
