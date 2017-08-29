import smtplib
import getpass


def connect_to_server():
    """
    Connects to gmail server

    Returns
    -------
    server : smtplib.SMTP_SSL
        gmail email server
    """
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    return server


def get_credentials():
    """
    Gets email to be used and credentials to the email

    Returns
    -------
    credentials : dict
        Contains keys

        + email
        + password
    """
    credentials = {'email': '', 'password': ''}
    email = input('Which email would you like to use? (Enter q to exit)\n')
    if email == 'q':
        credentials['email'] = email
        return credentials

    password = getpass.getpass(
            'Please input the password to {}: '.format(email))
    credentials['email'] = email
    credentials['password'] = password
    return credentials


def login_to_server(server):
    """
    Attempts to log in to server until successfully
    authenticated or quit char is entered

    Parameters
    ----------
    server : smtplib.SMTP_SSL
        Server with which to authenticate

    Returns
    -------
    (authenticated, credentials['email']) : tuple
        + authenticated
            Boolean indicated whether client successfully authenticated
        + credentials['email']
            Email address of sender
    """
    authenticated = False
    for i in range(3):
        try:
            credentials = get_credentials()
            if credentials['email'] == 'q':
                break
            print('Authenticating...')
            server.login(credentials['email'], credentials['password'])
        except Exception as e:
            print('\n**********ERROR**********\n')
            print(e)
            print('Please try again\n')
        else:
            authenticated = True
            break
    return (authenticated, credentials['email'])
