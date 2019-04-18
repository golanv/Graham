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
    # Search for verbose flag
    verbose = 0
    tmpargs = []
    for arg in range(0, len(args)):
        if args[arg] == "-v" or args[arg] == "--verbose":
            verbose = 1
        else:
            tmpargs.append(args[arg])
    args = tmpargs

    # Validate args
    if not validate_sysargs(args):
        exit(0)
    arglength = len(sys.argv)

    # Process config
    config = configparser.ConfigParser()
    config.read('/etc/graham.conf')
    destPath = config['DEFAULT']['destination']
    pool = config['DEFAULT']['pool']
    disks = config['DEFAULT']['disk'].split(",")

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
            if verbose == 1:
                print("Copying disk snapshot to backup location...")
            disker.disk_copy()

            # Checksum
            if verbose == 1:
                print("Verifying disk backup integrity...")
            if (disker.disk_check_sum()):
                print("Disk " + disk + " backed up successfully!")   # Remove Line
            else:
                print("Disk " + disk + " backup failed!\nExiting...")            # Remove Line
                snapper.remove()
                exit(0)

            # Remove snapshot
            if verbose == 1:
                print("Removing snapshot...")
            snapper.remove()

            print("Disk backup completed successfully.")
            exit(0)
        elif arglength == 2:
            if sys.argv[1] == "--oneshot":
                # Copy disk
                if verbose == 1:
                    print("Copying disk snapshot to backup location...")
                disker.disk_copy()

                # Remove snapshot
                if verbose == 1:
                    print("Removing snapshot...")
                snapper.remove()

                if verbose == 1:
                    print("Disk backup completed successfully.")
                exit(0)
            elif sys.argv[1] == "--bz2":
                # Copy disk
                if verbose == 1:
                    print("Copying disk snapshot to backup location...")
                disker.disk_copy()

                # Checksum
                if verbose == 1:
                    print("Verifying disk backup integrity...")
                if (disker.disk_check_sum()):
                    print("Disk " + disk + " backed up successfully!")  # Remove Line
                else:
                    print("Disk " + disk + " backup failed!\nExiting...")  # Remove Line
                    snapper.remove()
                    exit(0)

                # Remove snapshot
                if verbose == 1:
                    print("Removing snapshot...")
                snapper.remove()

                # Compress disk
                if verbose == 1:
                    print("Compressing backup disk image...")
                disker.compress(dstSnap, dstSnap)

                # Remove uncompressed backup image
                if verbose == 1:
                    print("Removing backup disk...")
                disker.remove()

                if verbose == 1:
                    print("Disk backup completed successfully.")
                exit(0)
        elif arglength == 3:
            # Compress disk
            if verbose == 1:
                print("Compressing backup disk image...")
            disker.compress(srcSnap, dstSnap)

            # Remove snapshot
            if verbose == 1:
                print("Removing snapshot...")
            snapper.remove()

            if verbose == 1:
                print("Disk backup completed successfully.")
            exit(0)
        else:
            print("Use a valid argument.")
            exit(0)

        
if __name__ == '__main__':
    main(sys.argv)