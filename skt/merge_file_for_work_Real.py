import random
import shutil
import json
import os
import glob
import sys

#Real folder의 파일을 ID별 복사(이름 바뀜)
#Real folder, 저장할 폴더 입력

dir_path = sys.argv[1]
copy_path = sys.argv[2]

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        

        file_name = file_path.split('\\')[-1]


        ID = file_path.split('\\')[4]
        Device_or_Tablet = file_path.split('\\')[5]
        Meter = file_path.split("\\")[6]
        items = file_path.split("\\")[7]

        jpg_name = ID + "_" + Device_or_Tablet[3:] + "_" + Meter + "_" + items[3:] + "_" + file_name
        



        new_path = os.path.join(copy_path,ID)
        os.makedirs(new_path,exist_ok=True)

        new_jpg_file = os.path.join(new_path,jpg_name)
        shutil.copy2(file_path,new_jpg_file)