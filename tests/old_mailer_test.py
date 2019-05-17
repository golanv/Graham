import sys
sys.path.append("../")
from graham.classes.Disk import Disk
from graham.classes.Mailer import Mailer
import sys
import smtplib
from email.mime.text import MIMEText

mailFrom = ''
rcptTo = ''
subject = 'Mailer() test'
text = 'Test for the Mailer() Python class'
server = 'localhost'


def main(args):
    #mail = Mailer(mailFrom, rcptTo, subject, text, server)
    sendtextmail(mailFrom, rcptTo, subject, text, server)


def sendtextmail(mailFrom, rcptTo, subject, text, server):
    msg = MIMEText(text)
    msg['From'] = mailFrom
    msg['Subject'] = subject
    msg['To'] = rcptTo
    smtp = smtplib.SMTP(server)
    smtp.sendmail(mailFrom, [rcptTo], msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    main(sys.argv)
