import os
import shutil
import sys

ori_root = sys.argv[1]
compare_root = os.listdir(sys.argv[2])
save_root = sys.argv[3]

for (ori_root, ori_directories, ori_files) in os.walk(ori_root):
        for ori_file in ori_files:
            ori_file_path = os.path.join(ori_root, ori_file)
            ori_file_name = ori_file_path.split('\\')[-1]

            if ori_file_name in compare_root:
                new_path = os.path.join(save_root,ori_file_name)
                shutil.copy2(ori_file_path,new_path)