#이미지만 다른 폴더로 복사

import os
import shutil
import sys
orilist = os.listdir(sys.argv[1])
savelist = os.listdir(sys.argv[2])
zxc = []
for i in orilist:
    name,ext = os.path.splitext(i)
    if ext == ".jpg":
        #zxc = "".join(name)+ext
        imgpath = os.path.join(sys.argv[1],i)
        savepath = os.path.join(sys.argv[2],i)
        shutil.copy(imgpath,savepath)
