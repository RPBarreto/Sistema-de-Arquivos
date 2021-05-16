# -*- coding: utf-8 -*-
import os

def filesize(path):
    size = os.path.getsize(path)
    return size