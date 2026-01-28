import glob
import cv2
import numpy as np
import os
import imageio.v2 as imageio

DATA_FOLDER = r"C:\Users\Erik\PycharmProjects\PushBroom\data"
PREFIX = "frame-"
OUTPUT_FILE = "pushbroom.png"
GIF_FILE = "pushbroom.gif"
FPS = 300
frames = []


def main():
    paths = sorted(glob.glob(os.path.join(DATA_FOLDER, "*")))
    paths = [p for p in paths if os.path.basename(p).startswith(PREFIX)]

    if not paths:
        raise FileNotFoundError(f"No files starting with '{PREFIX}' found in {DATA_FOLDER}")

    im0 = cv2.imread(paths[0])
    if im0 is None:
        raise ValueError(f"Could not read first image: {paths[0]}")

    h, w, c = im0.shape
    row = h // 2

    out = np.empty((len(paths), w, c), dtype=im0.dtype)
    out[0] = im0[row, :, :]

    below_h = h - (row + 1)
    display = np.zeros((below_h, w, c), dtype=im0.dtype)  # starts empty/black

    for i, p in enumerate(paths[1:], start=1):
        im = cv2.imread(p)
        if im is None:
            raise ValueError(f"Could not read image: {p}")
        if im.shape[:2] != (h, w):
            raise ValueError(f"Image size mismatch for {p}: got {im.shape[:2]}, expected {(h, w)}")

        scan = im[row, :, :]     # (w, c) 1-pixel row
        out[i] = scan


        if below_h > 0:
            display[1:, :, :] = display[:-1, :, :]
            display[0, :, :] = scan

        overlay = im.copy()

        if below_h > 0:
            overlay[row + 1:, :, :] = display

        # Draw scanline indicator on top (1px thick)
        cv2.line(overlay, (0, row), (w - 1, row), (0, 0, 255), 1)

        frames.append(cv2.cvtColor(overlay, cv2.COLOR_BGR2RGB))


    cv2.imwrite(OUTPUT_FILE, out[::-1])
    print(f"Wrote {OUTPUT_FILE}")

    imageio.mimsave(GIF_FILE, frames, fps=FPS)
    print(f"Wrote {GIF_FILE}")


if __name__ == "__main__":
    main()
