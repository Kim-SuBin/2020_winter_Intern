import numpy as np
import cv2 as cv
import os

# Color
red = (0,0,255)

# Read image file list in directory
path_img = './img' # Set image directory path
img_file_list = os.listdir(path_img) # Read file list in path
img_file_list.sort()

# Read vector file list in directory
path_vector = './vector'
vector_file_list = os.listdir(path_vector) 
vector_file_list.sort()

# Store light status (0:Green, 1:Red)
light_list=[0]*3

#------test code-----------------------------------------

# Read image
image = "./img/{}".format(img_file_list[0]) #_1.JPG
img = cv.imread(image, cv.IMREAD_COLOR)

# Open vector_file_list
f = open("./vector/{}".format(vector_file_list[0]), "r") # read mode
vector_list = []
while(1):
	line = f.readline()
	if not line: break
	else:
		vector_list = line.split()
		vector_list = [int(i) for i in vector_list]


# Create red rectangle
cv.rectangle(img, (vector_list[0], vector_list[1]), (vector_list[2], vector_list[3]), red, 3)
	# file, (start_x, start_y), (last_x, last_y), (B,G,R), line thickness

cv.imshow("result", img)
cv.waitKey(0)
