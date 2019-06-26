# Graham
Project Graham is a python program for backing up KVM virtual machines on LVM.

### Automation
If running Graham from a cron job, you may want to call graham from a bash script (useful for mounting disks, calling rsync to move backups, etc).  Keep in mind that PATH= will need to be set, as parts of Graham do call local programs.  If PATH= is not set, then Graham will fail if called from cron.  Please consider the following model:

```bash
#!/bin/bash
# /usr/local/sbin/graham
PATH=/usr/bin:/usr/sbin

# Mount backup disks
mount /dev/sdb1 /mnt/backup

# Call Graham
/usr/bin/python3 /path/to/graham/graham --bz2 --oneshot -v &&

# rsync backups
rsync -avhup /mnt/backup/* backupser@backuphost.example.com:/backup/
```

A sample cron job:

```
#Mins   Hours   Days    Months  Day of week     Command
0       0       *       *       6             /usr/local/sbin/graham &> /var/log/graham-backup.log
```