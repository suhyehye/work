import random
import shutil
import json
import os
import glob
import sys

#json 폴더, 저장 폴더 입력

alturk_folder = sys.argv[1]
save_root = sys.argv[2]
for (root, directories, files) in os.walk(alturk_folder):
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root,file)
            with open(file_path, "r",encoding='UTF-8') as f:
                data = json.load(f)
    
                points = data['objects'][0]['points']
                x = points[0]['x']
                y = points[0]['y']
                x2 = points[1]['x']
                y2 = points[1]['y']
                w = x2-x
                h = y2-y
                landmark_list = []
                for i in range(106):
                    landmark_list.append([0,0,1])

                my_dict = [{'landmark':landmark_list,
                            'box': {'x':x,
                            'y': y,
                            'w':w,
                            'h':h}}]

                
                new_path = os.path.join(save_root, file)

                with open(new_path,'w') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)

                




    
