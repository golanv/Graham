import sys
sys.path.append("../")
from graham.classes.Mailer import Mailer
import configparser

# Process config
config = configparser.ConfigParser()
config.read('/etc/graham.conf')

sendmail = config['MAIL']['sendmail']
mail_from = config['MAIL']['mail_sender']
rcpt_to = config['MAIL']['mail_recipient']
server = config['MAIL']['server']
msg = "See subject!"

# Send mail
subject = "[graham] Backup of disk complete"
mailer = Mailer(mail_from, rcpt_to, subject, msg, server)
mailer.sendtextmail()
