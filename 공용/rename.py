import concurrent.futures
import glob
import os
import sys
from os.path import basename, dirname, join
from sys import argv

import cv2
import numpy as np

base = lambda x: basename(x).split(".")[0]


if __name__ == '__main__':
    root = sys.argv[1]
    src = sys.argv[2]
    dst = sys.argv[3]
    os.chdir(root)

    for file in glob.iglob('**/*.*', recursive=True):
        os.rename(file, join(dirname(file), basename(file).replace(src, dst)))
