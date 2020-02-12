import numpy as np
import cv2 as cv
import os

# Color
red = (0, 0, 255)

# Read image file list in directory
path_img = './img'  # Set image directory path
img_file_list = os.listdir(path_img)  # Read file list in path
img_file_list.sort()


# Read vector file list in directory
'''
path_vector = './vector'
vector_file_list = os.listdir(path_vector)
vector_file_list.sort()
'''
# Store light status (0:Green, 1:Red)
light_list = [0] * 3

# ------test code-----------------------------------------

# Open vector_file_list
cnt = 0

vector_list = []
f = open("./vector/vec.txt", "r")  # Read vector values
while 1:
    line = f.readline()
    if not line:
        break
    else:
        vector_list = line.split()
        vector_list = [int(i) for i in vector_list]


def extractor(img, cnt):
    # Crop image
    cropped_img = img[vector_list[cnt+1]:vector_list[cnt+3], vector_list[cnt]:vector_list[cnt+2]]
    return cropped_img


for j in range(0,len(img_file_list)):
    for i in range(0, 3):
        image = "./img/{}".format(img_file_list[j]) 
        img = cv.imread(image, cv.IMREAD_COLOR)
        # print(vector_list[cnt], vector_list[cnt+1],vector_list[cnt+2], vector_list[cnt+3])
        cv.rectangle(img, (vector_list[cnt], vector_list[cnt+1]), (vector_list[cnt+2], vector_list[cnt+3]), red, 3) # Draw rectangle (Part of parking space)
        img = extractor(img, cnt)
        file_name_path = './crop_img/' + str(j) + '_' + str(i) + '_' + 'test.JPG' # Store crop image
        cv.imwrite(file_name_path, img)
        cnt = cnt + 4
