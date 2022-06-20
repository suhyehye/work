import sys
import glob
import os
import shutil

a_folder = sys.argv[1]
b_folder = sys.argv[2]

for a_file in glob.glob(os.path.join(a_folder,'*.jpg')):
   a_file_name = a_file.split('\\')[-1][:-4]
   print(a_file_name)
   print('-------------')

   

   for b_file in glob.glob(os.path.join(b_folder,'*.json')):
       b_file_name = b_file.split('\\')[-1][:-13]
       print(b_file_name)
    

       if a_file_name == b_file_name:
           shutil.copy2(a_file, b_folder)
           print('same')

           

