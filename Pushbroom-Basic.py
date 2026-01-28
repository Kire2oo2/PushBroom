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

    #allocating array size for the given image sizes and number
    out = np.empty(
        (len(paths), im0.shape[1], im0.shape[2]),
        dtype=im0.dtype
    )

    #extract the same row from every image and put in out array
    out[0] = im0[row, :, :]
    print(im0[row, :, :])
    for i, p in enumerate(paths[1:], start=1):
        im = cv2.imread(p)
        out[i] = im[row, :, :]
        #print(f"Processed {os.path.basename(p)}")

    cv2.imwrite(OUTPUT_FILE, out[::-1])
    print(f"Wrote {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

#overlap imaging
#RGB
#sat data tidsforyvning mellom frekvenser