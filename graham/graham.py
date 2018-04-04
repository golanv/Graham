#!/usr/bin/env python3

from classes.Disk import Disk
from classes.Snapshot import Snapshot
import sys
import configparser
from time import sleep

def main(args):
    #print(args)
    destPath = None
    disks = []
    pool = None
    
    config = configparser.ConfigParser()
    config.read('/etc/graham.conf')
    destPath = config['DEFAULT']['destination']
    pool = config['DEFAULT']['pool']
    disks = config['DEFAULT']['disk'].split(",")
    
    for disk in disks:
        # Create snapshot object instance
        Snapper = Snapshot (pool, disk)
        snap = Snapper.getSnapshot()
        #print(snap)                                     # Remove line
        
        # More vars
        srcSnap = pool + snap
        dstSnap = destPath + snap
        
        # Create Snapshot
        Snapper.create()
        sleep(10)
        #print("Destination Path: " + destPath)          # Remove line
        
        # Copy disk
        Disk().diskCopy(srcSnap, dstSnap)
        
        # Checksum
        if (Disk().diskCheckSum(srcSnap, dstSnap)):
            print("Disk " + disk + " backed up successfully")   # Remove Line
        else:
            print("Disk " + disk + " backup failed")            # Remove Line

        
if __name__ == '__main__':
    main(sys.argv)
