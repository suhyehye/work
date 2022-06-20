# Real 폴더 내의 모든 파일을 하나로 합쳐줌(이름바뀜)
# Real folder, 저장할 폴더 입력

import pandas as pd
import numpy as np
import json
import os
import glob
import shutil
import sys

dir_path = sys.argv[1]
copy_path = sys.argv[2]

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        tmp = file_path.split('\\')
        file_name = tmp[6][3:]+'_'+tmp[5][3:]+'_'+tmp[-4][3]+'_'+tmp[-3]+'_'+tmp[-2][3:]+'_'+tmp[-1]
        copy_jpg = os.path.join(copy_path,file_name)
        if not os.path.exists(copy_jpg):
            shutil.copy2(file_path,copy_jpg)