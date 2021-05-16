import os

def filesize(path):
    size = os.path.getsize(path)
    return size