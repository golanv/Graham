#!/usr/bin/env python3.4
# Python 3 support only
# Author: golanv
# Version 0.2
import subprocess
import time
import os
from time import strftime
from modules.sendtextmail import sendtextmail
from modules.filecheck import checksum

# Mail variables
mailFrom = ''
rcptTo = ''
# subject = ''
subjSuccess = ''
subjFail = '.'
text = 'See Subject!'
server = 'localhost'

# Sync Variables
spath = '/backup/'
dpath = '/storage/images/'
rhost = 'root@'

# VM Variables
vm1 = ''
vm2 = ''
vm3 = ''
vm4 = ''
vm5 = ''
vm6 = ''
vm7 = ''
vm8 = ''
vm9 = ''

# VM original disk image paths
vm1_src_path = '/dev/vg0/' + vm1
vm2_src_path = '/dev/vg0/' + vm2
vm3_src_path = '/dev/vg0/' + vm3
vm4_src_path = '/dev/vg0/' + vm4
vm5_src_path = '/dev/vg0/' + vm5
vm6_src_path = '/dev/vg0/' + vm6
vm7_src_path = '/dev/vg0/' + vm7
vm8_src_path = '/dev/vg0/' + vm8
vm9_src_path = '/dev/vg0/' + vm9

# You must use the full path and filename here"
# vm1_dst_path = '/backup/Louis-' + strftime("%d_%a_%b_%Y_%H:%M:%S") + '.img'
vm1_dst_path = '/backup/' + vm1 + '.img'
vm2_dst_path = '/backup/' + vm2 + '.img'
vm3_dst_path = '/backup/' + vm3 + '.img'
vm4_dst_path = '/backup/' + vm4 + '.img'
vm5_dst_path = '/backup/' + vm5 + '.img'
vm6_dst_path = '/backup/' + vm6 + '.img'
vm7_dst_path = '/backup/' + vm7 + '.img'
vm8_dst_path = '/backup/' + vm8 + '.img'
vm9_dst_path = '/backup/' + vm9 + '.img'



def compare_hash(x, y, z):
    if checksum(x) == checksum(y):
        print('Backup Successful')
        sendtextmail(mailFrom, rcptTo, '[' + z + '] Disk backup successful.', text, server)
    else:
        print('Backup Unsuccessful')
        sendtextmail(mailFrom, rcptTo, '[' + z + '] Disk backup failed.', text, server)


def backup(vm, vm_src_path, vm_dst_path):
    print(('Shutting down ' + vm))
    subprocess.call('virsh shutdown ' + vm, shell=True)
    time.sleep(60)
    print(('Backing up ' + vm + '. This may take a really long time...'))
    subprocess.call('dd if=' + vm_src_path + ' of=' + vm_dst_path, shell=True)
    print(('Verifying backup of ' + vm + '... You should probably go do something else for a while.'))
    compare_hash(vm_src_path, vm_dst_path, vm)
    print(('Restarting ' + vm))
    subprocess.call('virsh start ' + vm, shell=True)
    print('Compressing image file...')
    subprocess.call('gzip ' + vm_dst_path, shell=True)
    print('Backup of ' + vm + ' complete')

# Defining the path to run shell commands.  This is needed to run script as a cron job.
os.environ['PATH'] = '/bin:/usr/bin:/usr/sbin'

# Add other vm variables here.  This actually runs the backup commands.
backup(vm1, vm1_src_path, vm1_dst_path)
#backup(vm2, vm2_src_path, vm2_dst_path)
backup(vm3, vm3_src_path, vm3_dst_path)
#backup(vm4, vm4_src_path, vm4_dst_path)
#backup(vm5, vm5_src_path, vm5_dst_path)
backup(vm6, vm6_src_path, vm6_dst_path)
#backup(vm7, vm7_src_path, vm7_dst_path)
backup(vm8, vm8_src_path, vm8_dst_path)
#backup(vm9, vm9_src_path, vm9_dst_path)


cmd1 = subprocess.call('rsync -avhup --rsh="ssh -p22" ' + spath + ' ' + rhost + dpath, shell=True)
cmd2 = subprocess.call('rm -f ' + spath + '*', shell=True)

if cmd1 == 0 & cmd2 == 0:
    sendtextmail(mailFrom, rcptTo, subjSuccess, text, server)
else:
    sendtextmail(mailFrom, rcptTo, subjFail, text, server)
