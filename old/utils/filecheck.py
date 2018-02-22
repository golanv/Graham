# -*- coding: utf-8 -*-
import hashlib


def checksum(n):
    file_f = open(n, 'rb')
    hash_h = hashlib.new('sha1')
    for chunk in chunker(file_f, 512):
        hash_h.update(chunk)
    print((hash_h.hexdigest()))
    return hash_h.hexdigest()
    file_f.close()

# Divides file into chucks in order to generate a hash.


def chunker(fileobj, size):
    while True:
        data = fileobj.read(size)
        if not data:
            return
        yield data


def compare_hash(x, y):
    if checksum(x) == checksum(y):
        return True
    else:
        return False
