#spoof folder 생성
#생성하고자하는 폴더 위치 입력

#ID_0001부터 ID_0200까지 한번에 생성됨

import os
import shutil
import datetime
import time
import sys

work_dir = sys.argv[1]
def add_id(work_dir,i):
    saveRootDir = os.path.join(work_dir)
    
    if not os.path.exists(saveRootDir):
        os.mkdir(saveRootDir)
        clipNameDirPath = os.path.join(saveRootDir,i)
        os.mkdir(clipNameDirPath)
        
    else:
        clipNameDirPath = os.path.join(saveRootDir,i)
        if not os.path.exists(clipNameDirPath):
            os.mkdir(clipNameDirPath)
            
    path_id = os.path.join(work_dir,i)         
    return path_id


spoof_labels = ['00.Print_Attack','01.Replay_Attack']
print_at = ['00.Paper','01.Photo']
print_labels = ['00.Flat1','01.Flat2','02.Flat3','03.Band']
replay_labels = ['00.Smartphone','01.Notebook','02.Video']


def make_folder(path_id):
    for spoof in spoof_labels:
        if spoof == '00.Print_Attack':

            for print_label in print_labels:
                saveRootDir = os.path.join(path_id,spoof,print_label)
                os.makedirs(saveRootDir)

        if spoof == '01.Replay_Attack':
            for replay_label in replay_labels:
                saveRootDir = os.path.join(path_id, spoof, replay_label)
                os.makedirs(saveRootDir)


def make_folder(path_id):
    for spoof in spoof_labels:
        if spoof == '00.Print_Attack':
            
            for pr in print_at:

                for print_label in print_labels:
                    saveRootDir = os.path.join(path_id,spoof,pr,print_label)
                    os.makedirs(saveRootDir,exist_ok=True)

        if spoof == '01.Replay_Attack':
            for replay_label in replay_labels:
                saveRootDir = os.path.join(path_id, spoof, replay_label)
                os.makedirs(saveRootDir,exist_ok=True)

for i in range(1,201):
    if i <10:
        id = 'ID_000'+str(i)
        path_id = add_id(work_dir,id)
        make_folder(path_id)

    elif i<100:
        id = 'ID_00'+str(i)
        path_id = add_id(work_dir,id)
        make_folder(path_id)

    else:
        id = 'ID_0'+str(i)
        path_id = add_id(work_dir,id)
        make_folder(path_id)

    print(id)                