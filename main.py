import numpy as np
from numpy import array
from PIL import Image
from sys import argv

if len(argv) < 4:
    print("Error! Not enough parameters")
    exit(-1)

try:
    image = Image.open(argv[2])
except:
    print("No such image!")
    exit(-1)
image_arr = array(image)
factor = float(argv[1])
new_im = Image.new(mode = "RGB", size = (int(image_arr.shape[1]*factor), int(image_arr.shape[0]*factor)))
arr = array(new_im)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        myxc = i / arr.shape[0]
        myyc = j / arr.shape[1]
        coord1 = int(myxc*image_arr.shape[0])
        coord2 = int(myyc*image_arr.shape[1])
        arr[i][j][0] = image_arr[coord1][coord2][0]
        arr[i][j][1] = image_arr[coord1][coord2][1]
        arr[i][j][2] = image_arr[coord1][coord2][2]
new_im = Image.fromarray(arr)
new_im.save(argv[3])