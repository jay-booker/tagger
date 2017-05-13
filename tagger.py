#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
from shutil import copy

from numpy import *


def taggerTest():
    classList=[]
    for i in range(1,10):
        file_path = ur'blog/%d.txt'%i
        docList=open(file_path).read()  #打开文本文件
        classList[i]=raw_input()
        if classList[i] == 1:
            dest_dir = ur'result/market'
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)
            copy(file_path, dest_dir)
        elif classList[i] == 2:
            dest_dir = ur'result/plate'
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)
            copy(file_path, dest_dir)
        else:
            dest_dir = ur'result/simple'
            if not os.path.isdir(dest_dir):
                os.makedirs(dest_dir)
            copy(file_path, dest_dir)


if __name__ == '__main__':
    taggerTest()
