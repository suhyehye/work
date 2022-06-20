import random
import shutil
import json
import os
import glob
import sys

# Spoof 폴더의 파일을 ID별로 복사해줌(이름바뀜)
# 원본 폴더, 저장폴더 입력

dir_path = sys.argv[1]
copy_path = sys.argv[2]

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        file_path = os.path.join(root, file)
        

        file_name = file_path.split('\\')[-1]


        ID = file_path.split('\\')[4]
        print_or_replay = file_path.split('\\')[5]

        if print_or_replay == '00.Print_Attack':
            paper_or_photo = file_path.split('\\')[6] 
            flat = file_path.split('\\')[7]
            jpg_name = ID + "_" + print_or_replay[3:-7]  + "_" + paper_or_photo[3:] + "_" + flat[3:] + "_" + file_name



        if print_or_replay == '01.Replay_Attack':
            item  = file_path.split('\\')[6]
            jpg_name = ID + "_" + print_or_replay[3:-7]+ "_" + item[3:]+"_" + file_name


        new_path = os.path.join(copy_path,ID)
        os.makedirs(new_path,exist_ok=True)

        new_jpg_file = os.path.join(new_path,jpg_name)
        shutil.copy2(file_path,new_jpg_file)