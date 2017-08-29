#!/usr/bin/env python

import sys
from utils import parse, server, sendmail

'''
This is a script to send emails from python
'''

exception_string = """\
Usage: ./email_script.py <plaintext_file> <html_file> [options]
Use -h to show help"""

opts, args = parse.process_arguments()
try:
    if len(args) < 1:
        raise Exception(exception_string)
except Exception as e:
    print(e)
    sys.exit()

opts = vars(opts)
subject = input('What would you like the subject of the email to be?\n')
text_file = parse.process_message(args[0])
html_file = parse.process_message(args[1])
message = {'text': text_file, 'html': html_file}

print('Connecting to mail server...')
mail_server = server.connect_to_server()
logged_in, email = server.login_to_server(mail_server)

if logged_in:
    print('Successfully authenticated, sending mail...')
    receipients = parse.process_receipients(opts['email_csv'])
    for receipient in receipients:
        sendmail.send_message(mail_server, email, receipient, subject, message)
    print('Successfully finished sending email')
print('Exiting')

mail_server.quit()
