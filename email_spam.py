import smtplib
from getpass import getpass
import time

gmail_user = input('Email: ')
gmail_password = getpass('Password: ')

sent_from = gmail_user
to = gmail_user
subject = 'Subject'
body = "Message"

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

n = int(input('How many times you want to send this email: '))
sec = int(input('And how many second apart do you want to send it: '))

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    for _ in range(n):
        time.sleep(sec)
        server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except Exception as e:
    print(e)
