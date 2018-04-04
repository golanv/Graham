class Disk:
    srcPath = None
    destPath = None
    srcDisk = None
    destDisk = None
    
    def __init__(self, path, src):
        self.srcPath = path
        self.srcDisk = src
