import glob
import cv2
import numpy as np
import os

DATA_FOLDER = "C:\\Users\\Erik\\PycharmProjects\\PushBroom\\data"
PREFIX = "frame-"
OUTPUT_FILE = "pushbroom.png"


def main():
    paths = sorted(glob.glob(f"{DATA_FOLDER}/*"))

    paths = [
        p for p in paths
        if os.path.basename(p).startswith(PREFIX)
    ]

    im0 = cv2.imread(paths[0])
    h = im0.shape[0]
    row = h // 2
    out = np.empty((len(paths), im0.shape[1], im0.shape[2]), dtype=im0.dtype)
    out[0] = im0[row, :, :]

    for i, p in enumerate(paths[1:], start=1):
        im = cv2.imread(p)
        out[i] = im[row, :, :]

    cv2.imwrite(OUTPUT_FILE, out)
    print(f"Wrote {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
