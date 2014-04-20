#! /usr/bin/python
# File Indexer
# It searches for all file types, creates type specific directories
# and moves the files inside those directories.
#
# Author: Abhilash Raj
# Date: 20th April, 2014
##################################################################

import os
import sys
import shutil

dir = sys.argv[1]
types = []
video_types = ['mp4', 'mov', 'avi']
for file in os.listdir(dir):
    try:
        if '.' in file:
            extension = file.split('.')[-1]
            if extension not in types:
                    types.append(extension)
    except IndexError:
        pass

for type in types:
    try:
        os.mkdir(dir + '/' + type)
    except OSError:
        pass

for file in os.listdir(dir):
    if '.' in file:
        extension = file.split('.')[-1]
        shutil.move(dir + '/' + file, '{}/{}/'.format(dir, extension))
print types
