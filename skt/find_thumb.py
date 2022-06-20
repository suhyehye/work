#입력한 폴더의 thumb.db 파일 위치 반환
#thumb 파일 찾고자 하는 폴더 입력

import os
import shutil
import datetime
import time
import glob
import sys

real_files = sys.argv[1]
for (root, directories, files) in os.walk(real_files):
    for file in files:
        file_path = os.path.join(root, file)
        if '.jpg' not in file:
            print(file_path)