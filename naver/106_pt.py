import json
import glob
import os

json_106 = glob.glob(r'C:\Users\alchera\Desktop\Naver_landmark\00.train\106-points_VIET\*\*.json')
for json_file in json_106:
    file_name = json_file.split("\\")[-1]
    with open(json_file, "r") as f:
        data = json.load(f)
        points = data[0]['points']


        id = 0
        
        data_list = []
        for i in points:
            id = id+1
            x = i[0]
            y = i[1]

            if i[2] == 0:

                visible = "visiblePoint"
            else :
                visible = "invisiblePoint"

            my_dict = {"type":"Point"}

            my_dict["id"] = id
            my_dict["coordinates"] = [x,y]
            my_dict["properites"] = {"globaltype":visible}
            data_list.append(my_dict)

        data_dict = {"DataList":data_list,"WorkLoad": {}}
        print(data_dict)

        with open(r'C:\Users\alchera\Desktop\Naver_landmark\05.납품\106-pt\{}.json'.format(file_name),'w') as f:
            json.dump(data_dict, f, ensure_ascii=False, indent=4)
