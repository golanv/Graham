# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText

# Be sure to define the following variables in your script:
# mailFrom = ''
# rcptTo = ''
# subject = ''
# text = ''
# server = ''


def sendtextmail(mailFrom, rcptTo, subject, text, server):
    msg = MIMEText(text)
    msg['From'] = mailFrom
    msg['Subject'] = subject
    msg['To'] = rcptTo
    smtp = smtplib.SMTP(server)
    smtp.sendmail(mailFrom, [rcptTo], msg.as_string())
    smtp.quit()
