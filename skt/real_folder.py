#ID입력하면 폴더트리 생성됨
#폴더트리 생성할 폴더 입력


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

id = input("ID를 입력하세요 :")
path_id = add_id(work_dir, i = id)

meters = ['0.5m','1m','2m']
labels = ['00.Real','01.Spoof']
items = ['00.Original','01.Mask','02.Cap','03.Glasses','04.Sun-glasses']
spoof_labels = ['00.print','01.replay']
print_labels = ['00.plat1','01.plat2','02.plat3','03.band']
replay_labels = ['00.smartphone','01.notebook','02.tablet']
c_t = ['01.Device','02.Tablet']


folder_list = []
for c in c_t:
    for meter in meters:
        for item in items:
            saveRootDir = os.path.join(path_id,c)
            if not os.path.exists(saveRootDir):
                os.mkdir(saveRootDir)
                clipNameDirPath = os.path.join(saveRootDir,meter,item)
                folder_list.append(clipNameDirPath)
                os.makedirs(clipNameDirPath)
            
   
            else:
                clipNameDirPath = os.path.join(saveRootDir,meter,item)
                if not os.path.exists(clipNameDirPath):
                    os.makedirs(clipNameDirPath)
                    folder_list.append(clipNameDirPath)