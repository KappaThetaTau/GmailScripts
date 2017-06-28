import smtplib
import getpass


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
