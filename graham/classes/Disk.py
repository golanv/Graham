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
        if hashlib.sha256(src) == hashlib.sha256(dst):
            print("Disks are equal")
        else:
            print("Disks are not equal")           
