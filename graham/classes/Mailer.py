import smtplib
from email.mime.text import MIMEText


class Mailer:
    mail_from = None
    rcpt_to = None
    subject = None
    msg = None
    server = None
    
    def __init__(self, mail_from, rcpt_to, subject, text, server):
        self.mail_from = mail_from
        self.rcpt_to = rcpt_to
        self.subject = subject
        self.server = server
        self.msg = MIMEText(text)
        self.msg['From'] = mail_from
        self.msg['Subject'] = subject
        self.msg['To'] = rcpt_to

    def sendtextmail(self):
        smtp = smtplib.SMTP(self.server)
        smtp.sendmail(self.mail_from, [self.rcpt_to], self.msg.as_string())
        smtp.quit()
