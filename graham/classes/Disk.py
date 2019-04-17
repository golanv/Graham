import sys 
import shutil
import hashlib
import bz2
from shutil import copyfileobj
import os


class Disk:
    srcPath = None
    destPath = None
    srcDisk = None
    destDisk = None
    
    def __init__(self):
        return

    def set_src_path(self, srcpath):
        self.srcPath = srcpath

    def set_dst_path(self, dstpath):
        self.destPath = dstpath

    def set_src_disk(self, srcdisk):
        self.srcDisk = srcdisk

    def set_dst_disk(self, dstdisk):
        self.destDisk = dstdisk

    def diskCopy(self):
        try:
            shutil.copy2(self.srcPath + self.srcDisk, self.dstPath + self.srcDisk)
        except IOError as e:
            print("Unable to copy file. %s" % e)

    @staticmethod
    def diskCopy(src, dst):
        try:
            shutil.copy2(src, dst)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())

    @staticmethod
    def compress(dsk, snap, path):
        with open(snap, 'rb') as data:
            with bz2.BZ2File(path + dsk + ".bz2", 'wb') as outfile:
                copyfileobj(data, outfile)

    @staticmethod
    def remove(dsk):
        if (dsk):
            try:
                os.remove(dsk)
                print("Uncompressed backup image removed")
            except OSError as e:
                print("Error: %s - %s." % (e.filename,e.strerror))
        else:
            print("Sorry, I can not find $s file." % dsk)

    def diskCheckSum(self, src, dst):
        if self.checksum(src) == self.checksum(dst):
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
