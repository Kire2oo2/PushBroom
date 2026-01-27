import glob
import cv2
import numpy as np
import os

DATA_FOLDER = "C:\\Users\\Erik\\PycharmProjects\\PushBroom\\data"
PREFIX = "frame-"
OUTPUT_FILE = "pushbroom.png"
ROW_INDEX = -1

def main():
    paths = sorted(glob.glob(f"{DATA_FOLDER}/*"))

    paths = [
        p for p in paths
        if os.path.basename(p).startswith(PREFIX)
    ]

    imgs = []
    for p in paths:
        im = cv2.imread(p)
        if im is not None:
            imgs.append(im)

    h = imgs[0].shape[0]
    row = h // 2 if ROW_INDEX == -1 else ROW_INDEX

    out = np.concatenate(
        [im[row:row+1, :, :] for im in imgs],
        axis=0
    )

    cv2.imwrite(OUTPUT_FILE, out)
    print(f"Wrote {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
