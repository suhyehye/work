#인쇄용 사진 랜덤 추출
#0.5m 촬영본만 추출
#흑백사진 제거
#랜덤추출안된 ID만 복사

#Real folder, 저장할 폴더 입력

import random
import shutil
import json
import os
import glob
import sys

ori_path = glob.glob(os.path.join(sys.argv[1],"*"))
copy_path = sys.argv[2]

for ori in ori_path:
    ID = ori.split('\\')[-1]
    print(ID)
    file_path = os.path.join(ori,'./*/0.5m/*/*')
    file_folder = glob.glob(file_path)

    #흑백사진 제거
    file_for_random = [x for x in file_folder if 'IR' not in x]

    # 랜덤추출 개수 지정
    # 중복추출불가
    random_file = random.sample(file_for_random,4)
    new_path = os.path.join(copy_path,ID)
    if not os.path.exists(new_path):
        os.mkdir(new_path)

        for file in random_file:
            print(file)
            shutil.copy2(file,new_path)