import os,glob
from os.path import join,basename,dirname,splitext,isfile
import sys,shutil,json
import numpy as np
import cv2
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw,ImageFont
import matplotlib.pyplot as plt


blue, green, red = (255,0,0),(0,255,0),(0,0,255)
font = cv2.FONT_HERSHEY_COMPLEX

json_files = glob.glob(r"C:\Users\alchera\Desktop\Naver_landmark\Landmark_crop_img_json\134-points\*.json")


jpg_files = glob.glob(r"C:\Users\alchera\Desktop\Naver_landmark\Landmark_crop_img\*.jpg")



def pil_draw_point(image, point):
    x, y = point
    draw = ImageDraw.Draw(image)
    radius = 3
    draw.ellipse((x - 1/2*radius, y - 1/2*radius, x + 1/2*radius, y + 1/2*radius), fill=(0, 0, 255))

    return image

for json_file in json_files:

    json_name = json_file.split('\\')[-1][:-13]
    
    for jpg_file in jpg_files:
        jpg_name = jpg_file.split('\\')[-1][:-4]

        if json_name == jpg_name:
            with open(json_file, "r",encoding='UTF-8') as f:
                data = json.load(f)
                landmark = data[0]['points']
                image = Image.open(jpg_file)
           
                for land in landmark:
                    i = land[0]
                    j = land[1]
                    image = pil_draw_point(image,(i,j))
                
                plt.imshow(np.array(image))
   