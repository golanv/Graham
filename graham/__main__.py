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
        print("Copying disk snapshot to backup location...")
        Disk().diskCopy(srcSnap, dstSnap)
        
        # Checksum
        print("Verifying disk backup integrity...")
        if (Disk().diskCheckSum(srcSnap, dstSnap)):
            print("Disk " + disk + " backed up successfully!")   # Remove Line
        else:
            print("Disk " + disk + " backup failed!")            # Remove Line
            
        # Remove snapshot
        print("Removing snapshot...")
        Snapper.remove()

        # Compress disk
        print("Compressing backup disk image...")
        Disk().compress(disk, dstSnap, destPath)

        # Remove uncompressed backup image
        Disk().remove(dstSnap)

        
if __name__ == '__main__':
    main(sys.argv)
