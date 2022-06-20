if __name__ == '__main__':
    import sys
    import pickle
    import os
    json_root = sys.argv[1]
    img_root = json_root
    save_root = sys.argv[2]
    dirName = os.path.basename(json_root)
    save_root = os.path.join(save_root, dirName)
    if not os.path.exists(save_root):
        os.mkdir(save_root)
    img_list = glob.iglob(join(img_root, '*.jpg'))
    json_list = glob.iglob(join(json_root, '*.json'))
    pair_dict = defaultdict(list)
    for x in img_list:
        pair_dict[base(x)].append(x)
    for x in json_list:
        pair_dict[base(x)].append(x)
    # with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    for k, v in sorted(pair_dict.items()):
        if len(v) > 1:
            crop(v[0], v[1], save_root)
    os.chdir(save_root)
    img_list = glob.glob('**/*.jpg', recursive=True)
    with open('dump.pkl', 'wb') as f:
        pickle.dump(img_list, f)