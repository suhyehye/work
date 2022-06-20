import concurrent.futures
import glob
import os
import sys
from os.path import basename, dirname, join

import cv2
import numpy as np

base = lambda x: basename(x).split(".")[0]


# return last saved sampling number
def sample_frame(vid_path: str, save_root: str, rate=1) -> int:
    def save(frame, save_path):
        os.makedirs(dirname(save_path), exist_ok=True)
        res = cv2.imwrite(save_path, frame)

    new_base_name = vid_path.replace(os.sep, '_')

    cap = cv2.VideoCapture(vid_path)
    max_frame_number = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    i = 0
    while True:
        next_frame_number = i * rate
        cap.set(1, next_frame_number)

        ret, frame = cap.read()
        if not ret or max_frame_number < next_frame_number:
            return (i - 1) * rate
        next_frame_number_str = str(next_frame_number).zfill(8)
        save_path = join(save_root, new_base_name.replace('.avi', f"_{next_frame_number_str}.jpg"))

        # save_path = join(save_root, new_base_name.replace('.avi', f"_{i * rate}.jpg"))

        save(frame, save_path)
        i += 1


if __name__ == '__main__':
    root = sys.argv[1]
    save_root = sys.argv[2]
    os.chdir(root)

    for vid in glob.iglob('**/*.avi', recursive=True):
        vid_save_root = join(save_root, base(vid))
        sample_frame(vid, vid_save_root)
