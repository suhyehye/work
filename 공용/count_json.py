import os,glob
from os.path import join,basename,dirname
import sys,json
import pandas as pd

dir_path =sys.argv[1]
csv_path = sys.argv[2]
df = pd.DataFrame({'csv':[], 'instance num': [],'point num':[],'avg':[]})

for (root, directories, files) in os.walk(dir_path):
    for file in files:
        if '.json' in file:
            file_path = os.path.join(root, file)
            file_name = file_path.split('\\')[-1]

            label_list = []
            point_list = []
            with open(file_path, "r",encoding='UTF-8') as f:
                data = json.load(f)
                shapes = data['shapes']
                for i in shapes:
                    label = i['label']

                    label_list.append(label)

                my_list = []

                for j in shapes:
                    
                    points = j['points']
                    my_list.append(points)
                point_list.append( my_list)
                point_list = sum(point_list,[])
                point_list = sum(point_list,[])

                instance_count = len(label_list)
                point_count = len(point_list)
                avg = round(point_count/instance_count,1)

                

                data_to_insert = {'csv':file_name, 'instance num': instance_count,'point num':point_count,'avg':avg}
                df = df.append(data_to_insert, ignore_index=True)
                csv_name = 'bb.csv'
                csv_root = os.path.join(csv_path,csv_name)
                df.to_csv(csv_root)