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

        # Vars
        srcSnap = pool + snap
        dstSnap = destPath + snap

        # Setup Disk() instance variables
        disker.set_src_path(srcSnap)
        disker.set_dst_path(dstSnap)
        # disker.set_dst_disk(disk)

        # Create Snapshot
        snapper.create()
        sleep(10)

        # Copy disk
        print("Copying disk snapshot to backup location...")
        disker.disk_copy()
        
        # Checksum
        print("Verifying disk backup integrity...")
        if (disker.disk_check_sum()):
            print("Disk " + disk + " backed up successfully!")   # Remove Line
        else:
            print("Disk " + disk + " backup failed!")            # Remove Line
            
        # Remove snapshot
        print("Removing snapshot...")
        snapper.remove()

        # Compress disk
        print("Compressing backup disk image...")
        disker.compress(dstSnap, dstSnap)
        # disker.compress(disk, dstSnap, destPath)

        # Remove uncompressed backup image
        print("Removing backup disk...")
        disker.remove()

        
if __name__ == '__main__':
    main(sys.argv)
