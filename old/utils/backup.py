import filecheck
import time
import subprocess


fc = filecheck()


def diskBackup(vm, vm_src_path, vm_dst_path):
    subprocess.call('virsh shutdown ' + vm, shell=True)
    time.sleep(60)
    subprocess.call('dd if=' + vm_src_path + ' of=' + vm_dst_path, shell=True)
    if fc.compare_hash(vm_src_path, vm_dst_path, vm):
        return True
        subprocess.call('virsh start ' + vm, shell=True)
        subprocess.call('gzip ' + vm_dst_path, shell=True)
    else:
        return False
        subprocess.call('virsh start ' + vm, shell=True)
