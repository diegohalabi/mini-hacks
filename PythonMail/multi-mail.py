# send email from csv file, coding=utf-8
__author__ = 'Dr. Diego Halabi'

# load modules
import smtplib
import csv

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
        return Template(template_file_content)


# setup SMTP sender server
MY_ADDRESS = input('Your mail address: ')
PASSWORD = input('set your password: ')
s = smtplib.SMTP(host='smtp.office365.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)

# email body
message_template = read_template('template.txt')
signature = '\n--\nDr. Diego Halabi, PhD\n' \
            'Assistant Professor\n' \
            '\nDevelopmental Chronobiology Lab\n' \
            'Facultad de Medicina\n' \
            'Universidad Austral de Chile\n' \
            'Valdivia, Chile\n' \
            'Phone: +56 (63) 229 3928\n' \
            'Email: diego.halabi@uach.cl | P.O. Box: 567'

with open('mail_list.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # skip the header
    next(csv_reader)
    for row in csv_reader:
        msg = MIMEMultipart()

# compose the message
message = message_template.substitute(THESIS_TITLE=row[0],
                                      PERSON_GENDER=row[1],
                                      PERSON_NAME=row[2],
                                      SENDER_GENDER=row[3],
                                      SENDER_NAME=row[4],
                                      ADVISOR_GENDER=row[5],
                                      ADVISOR_NAME=row[6],
                                      DEADLINE=row[7]) + signature
print(message)

# setup the mail
msg['From'] = MY_ADDRESS
msg['To'] = row[8]
msg['Subject'] = 'Invita a participar en evaluación de Tesis Escuela Odontología UACh'

# add the message to the mail
msg.attach(MIMEText(message, 'plain'))

# send the mail
s.send_message(msg)
del msg

# quit STMP session
s.quit()
