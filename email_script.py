#!/usr/bin/env python

import sys
from parse import process_message, process_receipients, process_arguments
from server import connect_to_server, login_to_server
from sendmail import send_message

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

opts = vars(opts)
subject = args[0]
text_file = process_message(args[1])
html_file = ''
if opts['html']:
    html_file = process_message(opts['html'])
message = {'text': text_file, 'html': html_file}
print('Connecting to mail server...')
server = connect_to_server()
logged_in, email = login_to_server(server)
if logged_in:
    receipients = process_receipients(opts['email_csv'])
    for receipient in receipients:
        send_message(server, email, receipient, subject, message)

server.quit()
