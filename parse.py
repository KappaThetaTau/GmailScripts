import sys
import csv
from optparse import OptionParser


def process_arguments():
    usage = """
        Usage: %prog plaintext_filename html_filename [options]
    """
    parser = OptionParser(usage=usage, version='%prog 1.0')

    parser.add_option('-c', '--csv',
                      action='store',
                      dest='email_csv',
                      default='./emails/emails.csv',
                      help='csv containing email addresses')
    options, args = parser.parse_args()
    return (options, args)


def process_message(message_file):
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
    receipients = []
    with open(receipients_csv) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            full_name = row[0].split(' ', 1)
            if len(full_name) > 1:
                first_name = full_name[0]
                last_name = full_name[1]
            else:
                first_name = full_name[0]
                last_name = ''
            name = {'first': first_name, 'last': last_name}
            receipient = {'name': name, 'email': row[1]}
            receipients.append(receipient)
    f.close()
    return receipients
