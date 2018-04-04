import smtplib
from email.mime.text import MIMEText

class Mailer:
    server = None
    mailFrom = None
    rcptTo = None
    msg = None
    server = None
    
    def __init__(self, mailFrom, rcptTo, subject, text, server):
        self.server = server
        self.msg = MIMEText(text)
        self.msg['From'] = mailFrom
        self.msg['Subject'] = subject
        self.msg['To'] = rcptTo
        
        
    def sendtextmail(self):
        smtp = smtplib.SMTP(self.server)
        smtp.sendmail(self.mailFrom, [self.rcptTo], self.msg.as_string())
        smtp.quit()
