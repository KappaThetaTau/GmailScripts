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
Usage: ./email_script.py <plaintext_file> <html_file> [options]
Use -h to show help"""

opts, args = process_arguments()
try:
    if len(args) < 1:
        raise Exception(exception_string)
except Exception as e:
    print(e)
    sys.exit()

opts = vars(opts)
subject = input('What would you like the subject of the email to be?\n')
text_file = process_message(args[0])
html_file = process_message(args[1])
message = {'text': text_file, 'html': html_file}
print('Connecting to mail server...')
server = connect_to_server()
logged_in, email = login_to_server(server)
if logged_in:
    print('Successfully authenticated, sending mail...')
    receipients = process_receipients(opts['email_csv'])
    for receipient in receipients:
        send_message(server, email, receipient, subject, message)
print('Successfully finished sending email')

server.quit()
