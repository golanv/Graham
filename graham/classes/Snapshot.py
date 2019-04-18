import subprocess

class Snapshot():
    snapshot = None
    disk = None
    pool = None
    
    def __init__(self, pool, disk):
        self.pool = pool
        self.disk = disk
        self.snapshot = disk + "_snapshot"

    def get_snapshot(self):
        return self.snapshot
    
    def create(self):
        pool = self.pool
        snapshot = self.snapshot
        disk = self.disk
        subprocess.call("lvcreate -L1G -s -n" + pool + snapshot + " " + pool + disk, shell=True)
        
    def remove(self):
        pool = self.pool
        snapshot = self.snapshot
        disk = self.disk
        subprocess.call("lvremove " + pool + snapshot + " -y", shell=True)
