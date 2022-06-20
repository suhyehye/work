import os 
import glob 
import shutil
import sys
from os.path import dirname, join, basename 
from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':
    root = sys.argv[1]
    save_root = sys.argv[2]

    func = lambda x: '_'.join(basename(x).split('_')[:2])
    with ThreadPoolExecutor(4) as _exec:
        for x in glob.iglob(join(root, '**/*.jpg'), recursive=True):
            _dir = func(x)
            save_path = join(save_root, _dir, basename(x))
            if os.path.exists(save_path):
                continue
            print(save_path)
            os.makedirs(dirname(save_path), exist_ok=True)
            _exec.submit(shutil.copyfile, x, save_path)

        for x in glob.iglob(join(root, '**/*.json'), recursive=True):
            _dir = func(x)
            save_path = join(save_root, _dir, basename(x))
            if os.path.exists(save_path):
                continue
            print(save_path)
            os.makedirs(dirname(save_path), exist_ok=True)
            _exec.submit(shutil.copyfile, x, save_path)
