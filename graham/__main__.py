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
        # Create snapshot and disk object instances
        snapper = Snapshot(pool, disk)
        snap = snapper.getSnapshot()
        disker = Disk()
        #print(snap)                                     # Remove line

        # Setup Disk() instance variables
        disker.set_src_path(pool)
        disker.set_src_disk(snap)
        disker.set_dst_path(destPath)
        disker.set_dst_disk(disk)
        
        # More vars
        srcSnap = pool + snap
        dstSnap = destPath + snap
        
        # Create Snapshot
        snapper.create()
        sleep(10)
        #print("Destination Path: " + destPath)          # Remove line
        
        # Copy disk
        print("Copying disk snapshot to backup location...")
        disker.diskCopy(srcSnap, dstSnap)
        
        # Checksum
        print("Verifying disk backup integrity...")
        if (disker.diskCheckSum(srcSnap, dstSnap)):
            print("Disk " + disk + " backed up successfully!")   # Remove Line
        else:
            print("Disk " + disk + " backup failed!")            # Remove Line
            
        # Remove snapshot
        print("Removing snapshot...")
        snapper.remove()

        # Compress disk
        print("Compressing backup disk image...")
        disker.compress(disk, dstSnap, destPath)

        # Remove uncompressed backup image
        disker.remove(dstSnap)

        
if __name__ == '__main__':
    main(sys.argv)
