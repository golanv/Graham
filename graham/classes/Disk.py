import sys 
import shutil
import hashlib
import bz2
from shutil import copyfileobj
import os


class Disk:
    srcPath = None
    destPath = None
    
    def __init__(self):
        return

    def set_src_path(self, srcpath):
        self.srcPath = srcpath

    def set_dst_path(self, dstpath):
        self.destPath = dstpath

    def disk_copy(self):
        try:
            shutil.copy2(self.srcPath, self.destPath)
        except IOError as e:
            print("Unable to copy file: %s" % e)

    def remove(self):
        dsk = self.destPath
        if(dsk):
            try:
                os.remove(dsk)
                print("Uncompressed backup image removed")
            except OSError as e:
                print("Error: %s - %s." % (e.filename,e.strerror))
        else:
            print("Sorry, I can not find $s file." % dsk)

    def disk_check_sum(self):
        if self.checksum(self.srcPath) == self.checksum(self.destPath):
            return True
        else:
            return False

    def checksum(self, n):
        file_f = open(n, 'rb')
        hash_h = hashlib.sha256()
        for chunk in self.chunker(file_f, 4096):
            hash_h.update(chunk)
        print((hash_h.hexdigest()))
        file_f.close()
        return hash_h.hexdigest()

    @staticmethod
    def chunker(fileobj, size):
        while True:
            data = fileobj.read(size)
            if not data:
                return
            yield data

    @staticmethod
    def compress(source, dest):
        if "_snapshot" in dest:
            dest = dest.split("_snapshot")[0] + ".img"
        else:
            dest = dest + ".img"
        with open(source, 'rb') as data:
            with bz2.BZ2File(dest + ".bz2", 'wb') as outfile:
                copyfileobj(data, outfile)
