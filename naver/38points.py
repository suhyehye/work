import glob
import json

json_files = glob.glob(r"C:\Users\alchera\Downloads\json\*")


for file in json_files:
    if 'eye' in file:
        with open(file, "r") as f:
            data = json.load(f)
        
            points = data['points']
        
            my_list = []
            for i in points:
                landmark = []
                x = float(i['points']['x'])
                y = float(i['points']['y'])
                landmark.append(x)
                landmark.append(y)
                landmark.append(0)
                my_list.append(landmark)
        
            my_dict = [{'box': {'x':100,
                           'y':100,
                           'w':100,
                           'h':100},
                            'points':my_list}]
        
        
        tmp = file.split("\\")
        tmp2 = tmp[-1].split('_')
        with open(r'C:\Users\alchera\Downloads\38pt./{}.json'.format(tmp[-1][:-5]),'w') as f:
                json.dump(my_dict, f, ensure_ascii=False, indent=4)
