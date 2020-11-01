#!/usr/bin/env python3
import cv2
import sys

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

def aa(array, background=None):
    for y in range(len(array)):
        if background:
            print('\033[48;5;{}m'.format(background), end='')
        for x in range(len(array[0])):
            code = rgbToAnsi256(array[y, x][2], array[y, x][1], array[y, x][0])
            print('\033[38;5;{}m#'.format(code), end='')
        print('\033[0;00m')

img = cv2.imread(sys.argv[1])

width = 100
height = int(img.shape[0] / img.shape[1] * width * PROPORTION)
img = cv2.resize(img, (width, height))

aa(img, rgbToAnsi256(0, 0, 0))
