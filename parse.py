import sys
import csv


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
