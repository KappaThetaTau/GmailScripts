import sys
import csv
from optparse import OptionParser


def process_arguments():
    """
    Processes command line arguments

    Parameters
    ----------
    None : None
        There are no parameters for this function

    Returns
    -------
    (options, args) : tuple
        Contains option parameters and argument parameters in a Key-Value pair

        Note: must be parsed using vars(...) to get a Python dictionary
    """
    usage = """
        Usage: %prog plaintext_filename html_filename [options]
    """
    parser = OptionParser(usage=usage, version='%prog 1.0')

    parser.add_option('-c', '--csv',
                      action='store',
                      dest='email_csv',
                      default='./addresses/emails.csv',
                      help='csv containing email addresses. \n\
                      DEFAULT=\'./addresses/emails.csv\'')
    parser.add_option('-f', '--from-name',
                      action='store',
                      dest='from_name',
                      default='Theta Tau - Rush Chair',
                      help='display name shown as the sender. \n\
                      DEFAULT=\'Theta Tau - Rush Chair\'')
    parser.add_option('-d', '--delay',
                      action='store',
                      type='float',
                      dest='delay',
                      default=1.0,
                      help='seconds to wait between emails so gmail does not \
                      flag the account for spam. \n\
                      DEFAULT=1.0')
    options, args = parser.parse_args()
    return (options, args)


def process_message(message_file):
    """
    Reads message from a file

    Parameters
    ----------
    message_file : string
        Path to file containing the message

    Returns
    -------
    message : string
        String with contents of file
    """
    message = ""
    try:
        with open(message_file) as f:
            message = f.read()
        f.close()
    except Exception as e:
        print(e)
        sys.exit()
    return message


def process_receipients(receipients_csv):
    """
    Reads receipients from a file

    Blank lines are ignored, and rows without an email address
    (e.g. a header row) are skipped with a warning.  A row may
    also contain just an email address with no name.

    Parameters
    ----------
    receipients_csv : string
        Path to a csv containing receipients in format:

        name, email

    Returns
    -------
    receipients : list
        List of dictionaries with keys

        * name
        * email
    """
    receipients = []
    try:
        with open(receipients_csv) as f:
            reader = csv.reader(f, delimiter=',')
            for line_number, row in enumerate(reader, start=1):
                row = [field.strip() for field in row]
                if len(row) > 1:
                    full_name, email = row[0], row[1]
                elif len(row) == 1:
                    full_name, email = '', row[0]
                else:
                    continue
                if '@' not in email:
                    print('Skipping line {} of {}: no email address found'
                          .format(line_number, receipients_csv))
                    continue
                full_name = full_name.split(' ', 1)
                if len(full_name) > 1:
                    first_name = full_name[0].title()
                    last_name = full_name[1].title()
                else:
                    first_name = full_name[0]
                    last_name = ''
                name = {'first': first_name, 'last': last_name}
                receipients.append({'name': name, 'email': email})
    except Exception as e:
        print(e)
        sys.exit()
    return receipients
