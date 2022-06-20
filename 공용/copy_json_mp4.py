#mp4랑 이름이 같은 json 파일 복사하기
import os,glob
from os.path import join,basename,dirname,splitext,isfile
import sys,shutil
if __name__ == "__main__":
    mp4_root = sys.argv[1]
    json_root = sys.argv[2]
    #mp4_root = r'D:\Event_2\19-class_vod\check\sunset\1차'
    #json_root = r'D:\Event_2\19-class_vod\json\1차'
    mp4_list = glob.glob(join(mp4_root,'**/*.mp4'),recursive=True)
    for mp4 in mp4_list:
        f_name,ext = splitext(mp4)
        check_json_name = f_name.replace(mp4_root,json_root) + '.json'
        if isfile(check_json_name):
            copy_name = join(mp4_root,basename(check_json_name))
            print(copy_name)
            shutil.copy2(check_json_name,copy_name)