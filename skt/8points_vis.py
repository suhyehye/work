import os,glob
from os.path import join,basename,dirname,splitext,isfile
import sys,shutil,json
import numpy as np
import cv2
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw,ImageFont
import sys

## json, jpg 함께 있는 폴더, 복사 경로 순서대로 입력

blue, green, red = (255,0,0),(0,255,0),(0,0,255)
font = cv2.FONT_HERSHEY_COMPLEX


folder_1 = sys.argv[1]
copy_path = sys.argv[2]

file_folder = os.listdir(folder_1)
json_folder = [f for f in file_folder if f .endswith(r'.json')]
jpg_folder = [f for f in file_folder if f .endswith(r'.jpg')]

for json_file, jpg_file in zip(json_folder,jpg_folder):
    

    if json_file[:-13] == jpg_file[:-4]:
        json_path = os.path.join(folder_1, json_file)
        jpg_path = os.path.join(folder_1, jpg_file)

        with open(json_path, "r",encoding='UTF-8') as f:
                data = json.load(f)
                img = cv2.imread(jpg_path)

                box = data[0]['box']
                x = int(box['x'])
                y = int(box['y'])
                w = int(box['w'])
                h = int(box['h'])

                points = data[0]['landmark']
                points = [x for x in points if x[0] != 0]
                print(json_file)

                k = 0
                img = cv2.rectangle(img, (x,y,w,h), green, thickness=None, lineType=None, shift=None)

                for point in points:
                    i = np.int0(point[0])
                    j = np.int0(point[1])
                    k = k+1
                    img = cv2.circle(img,(i,j),3,red,-1)

                new_img_name = jpg_file[:-4]+"_vis.jpg"


                
                cv2.imwrite(os.path.join(copy_path,new_img_name),img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                    
