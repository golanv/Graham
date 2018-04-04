import sys 
import subprocess
import shutil
import hashlib

class Disk:
    srcPath = None
    destPath = None
    srcDisk = None
    destDisk = None
    
    #def __init__(self, path, src):
        #self.srcPath = path
        #self.srcDisk = src
        
    def diskCopy(self, src, dst):
        try:
            shutil.copy2(src, dst)
        except IOError as e:
            print("Unable to copy file. %s" % e)
        except:
            print("Unexpected error:", sys.exc_info())
            
    def diskCheckSum(self, src, dst):
        if self.checksum(src) == self.checksum(dst):
            return True
        else:
            return False
        
    def checksum(self, n):
        file_f = open(n, 'rb')
        hash_h = hashlib.new('sha256')
        for chunk in self.chunker(file_f, 4096):
            hash_h.update(chunk)
        print((hash_h.hexdigest()))
        return hash_h.hexdigest()
        file_f.close()

    def chunker(self, fileobj, size):
        while True:
            data = fileobj.read(size)
            if not data:
                return
            yield data
