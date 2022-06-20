import os,glob
from os.path import join,basename,dirname,splitext,isfile
import sys,shutil,json
import numpy as np
import cv2
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageDraw,ImageFont
import sys

# attrlabel 경로, jpg folder 경로, 저장 경로 입력

blue, green, red = (255,0,0),(0,255,0),(0,0,255)
font=ImageFont.truetype('C:/Windows/Fonts/malgun.ttf',25)

at_path = sys.argv[1]
jpg_folder = sys.argv[2]
save_root = sys.argv[3]

jpg_folder = glob.glob(os.path.join(jpg_folder,'./*'))

with open(at_path, "r",encoding='euc-kr') as f:
    data = json.load(f)
    jpg_name = data['attribute_list']
    for i in jpg_name:
        attribute = i['attribute']
        id = i['id']
        image_name = i['image_name'].split('/')[-1]
        #print(image_name)
        

        
        for jpg_file in jpg_folder:
            jpg_name = jpg_file.split('\\')[-1]
            # print(jpg_name)
            if image_name == jpg_name:
                mask = str((attribute[0]-1)/10)
                sunglass = str(attribute[1]-1)
                l_eye = str(attribute[2]-1)
                r_eye =str(attribute[3]-1)
                l_brow = str(attribute[4]-1)
                r_brow = str(attribute[5]-1)
                mouth = str(attribute[6]-1)
                lower_face = str((attribute[7]-1)/10)
                Mustache = str(attribute[8]-1)


                text = 'mask : {}\nsunglasses : {}\nleft_eye: {}\nright_eye: {}\nleft_brow : {}\nright_brow : {}\nmouth : {}\nlower_face : {}\nMustach : {}'.format(mask,sunglass, l_eye, r_eye, l_brow, r_brow, mouth, lower_face,Mustache)
                #print(text)
                img = Image.open(jpg_file)
                draw = ImageDraw.Draw(img)
                draw.text((50,50),text,font=font,fill=blue)

                new_img_name = jpg_name[:-4] + '_attribute.jpg'

                img.save(os.path.join(save_root,new_img_name))
                



                