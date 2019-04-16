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
    
    # def __init__(self, path, src):
        # self.srcPath = path
        # self.srcDisk = src

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
            except OSError as e:
                print("Error: %s - %s." % (e.filename,e.strerror))
        else:
            print("Sorry, I can not find $s file." % dsk)



    @staticmethod
    def diskCheckSum(self, src, dst):
        if self.checksum(src) == self.checksum(dst):
            return True
        else:
            return False

    @staticmethod
    def checksum(self, n):
        file_f = open(n, 'rb')
        hash_h = hashlib.sha256()
        for chunk in self.chunker(file_f, 4096):
            hash_h.update(chunk)
        print((hash_h.hexdigest()))
        return hash_h.hexdigest()
        file_f.close()

    @staticmethod
    def chunker(fileobj, size):
        while True:
            data = fileobj.read(size)
            if not data:
                return
            yield data
