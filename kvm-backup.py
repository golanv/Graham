#!/usr/bin/env python3
import os
from utils.mailer import sendtextmail
from utils import backup

bck = backup()

# Mail variables
mailFrom = ''
rcptTo = ''
subject = ''
text = ''
server = ''


# Synchronization Variables
spath = ''
dpath = ''
rhost = ''

# VM Name Variables
vm1 = ''

# VM original disk paths as array
vm1_src_path = ''

# VM destination disk paths as array
vm1_dst_path = ''

if bck.diskBack(vm, vm_src_path, vm_dst_path):
    sendtextmail(mailFrom, rcptTo, '[' + vm + '] Disk backup successful.', text, server)
else:
    sendtextmail(mailFrom, rcptTo, '[' + vm + '] Disk backup failed.', text, server)
