from classes.Disk import Disk
from classes.Snapshot import Snapshot
import sys
import configparser
from time import sleep


def validate_sysargs(arglist):
    if len(arglist) == 1:
        return True
    elif len(arglist) == 2:
        if (arglist[1] == "--bz2") or (arglist[1] == "--oneshot"):
            return True
    elif len(arglist) == 3:
        if (sys.argv[1] == "--oneshot" and sys.argv[2] == "--bz2") or \
                (sys.argv[1] == "--bz2" and sys.argv[2] == "--oneshot"):
            return True
        else:
            print("Invalid argument")
            return False
    else:
        print("Too many arguments!")
        return False


def main(args):
    if not validate_sysargs(args):
        exit(0)
    config = configparser.ConfigParser()
    config.read('/etc/graham.conf')
    destPath = config['DEFAULT']['destination']
    pool = config['DEFAULT']['pool']
    disks = config['DEFAULT']['disk'].split(",")
    arglength = len(sys.argv)
    
    for disk in disks:
        # Create snapshot and disk object instances
        snapper = Snapshot(pool, disk)
        snap = snapper.get_snapshot()
        disker = Disk()

        # Vars
        srcSnap = pool + snap
        dstSnap = destPath + snap

        # Setup Disk() instance variables
        disker.set_src_path(srcSnap)
        disker.set_dst_path(dstSnap)

        # Create Snapshot
        snapper.create()
        sleep(10)

        if arglength == 1:
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

            print("Disk backup completed successfully.")
            exit(0)
        elif arglength == 2:
            if sys.argv[1] == "--oneshot":
                # Copy disk
                print("Copying disk snapshot to backup location...")
                disker.disk_copy()

                # Remove snapshot
                print("Removing snapshot...")
                snapper.remove()

                print("Disk backup completed successfully.")
                exit(0)
            elif sys.argv[1] == "--bz2":
                # Copy disk
                print("Copying disk snapshot to backup location...")
                disker.disk_copy()

                # Checksum
                print("Verifying disk backup integrity...")
                if (disker.disk_check_sum()):
                    print("Disk " + disk + " backed up successfully!")  # Remove Line
                else:
                    print("Disk " + disk + " backup failed!")  # Remove Line

                # Remove snapshot
                print("Removing snapshot...")
                snapper.remove()

                # Compress disk
                print("Compressing backup disk image...")
                disker.compress(dstSnap, dstSnap)

                # Remove uncompressed backup image
                print("Removing backup disk...")
                disker.remove()

                print("Disk backup completed successfully.")
                exit(0)
        elif arglength == 3:
            # Compress disk
            print("Compressing backup disk image...")
            disker.compress(srcSnap, dstSnap)

            # Remove snapshot
            print("Removing snapshot...")
            snapper.remove()

            print("Disk backup completed successfully.")
            exit(0)
        else:
            print("Use a valid argument.")
            exit(0)

        
if __name__ == '__main__':
    main(sys.argv)
