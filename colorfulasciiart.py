#!/usr/bin/env python3
import argparse
import cv2

PROPORTION = 0.46

def rgbToAnsi256(r: int, g: int, b: int) -> int:
    if r == g and g == b:
        if r < 8:
            return 16
        elif 248 < r:
            return 231
        else:
            return round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)

def paint(array, background=None):
    for y in range(len(array)):
        if background:
            print('\033[48;5;{}m'.format(background), end='')
        for x in range(len(array[0])):
            code = rgbToAnsi256(array[y, x][2], array[y, x][1], array[y, x][0])
            print('\033[38;5;{}m#'.format(code), end='')
        print('\033[0;00m')

# argparse
ap = argparse.ArgumentParser()
ap.add_argument('image', help='path to input image')
ap.add_argument('-w', '--width', type=int, help='width of output image', default=100)
ap.add_argument('-b', '--background', help='specify background color like #ffffff', default=None)
args = ap.parse_args()

width = args.width
background = args.background
if background:
    bgrgb = [int(background.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]
    background = rgbToAnsi256(bgrgb[0], bgrgb[1], bgrgb[2])


img = cv2.imread(args.image)

height = int(img.shape[0] / img.shape[1] * width * PROPORTION)
img = cv2.resize(img, (width, height))

paint(img, background)
