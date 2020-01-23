import keyboard
import numpy as np
import cv2

img = cv2.imread("img/parkingLot.png", cv2.IMREAD_COLOR)

parkingList = [(167, 375), (221, 375), (275, 375), (329, 375), (383, 375),
               (437, 375), (491, 375), (545, 375), (599, 375), (653, 375),
               (707, 375), (761, 375), (815, 375), (116, 65), (170, 65),
               (224, 65), (278, 65), (389, 65), (443, 65), (497, 65),
               (551, 65), (605, 65)]
# parkingList[0]~[12]: a1~a13, [13]~[16]: b1~b4, [17]~[19]: c1~c3, [20]~[21]: d1~d2
# green = cv2.circle(img, parkingList[0], 7, (0, 255, 0), -1)
# red = cv2.circle(img, parkingList[0], 7, (0, 0, 255), -1)

for i in range(len(parkingList)):
    cv2.circle(img, parkingList[i], 7, (0, 255, 0), -1)

while 1:
    cv2.imshow("show", img)
    k = cv2.waitKey(0)
    if k == 27:  # esc key
        break
    elif k == ord('i'):
        key = int(input("press key:"))
        cv2.circle(img, parkingList[int(key) - 1], 7, (0, 0, 255), -1)
    elif k == ord('o'):
        key = int(input("press key:"))
        cv2.circle(img, parkingList[int(key) - 1], 7, (0, 255,0), -1)


    # key = keyboard.read_key()

    # if key == 'esc':
    #     #     break
    # elif key:
    #     cv2.circle(img, parkingList[int(key)-1], 7, (0, 0, 255), -1)
    #     a = int(input())
    #     cv2.circle(img, parkingList[a-1], 7, (0, 0, 255), -1)
    #     if keyboard.is_pressed("1"):
    #         cv2.circle(img, parkingList[a-1], 7, (0, 0, 255), -1)
    #     elif keyboard.is_pressed("1"):
    #         cv2.circle(img, parkingList[a-1], 7, (0, 0, 255), -1)


cv2.destroyAllWindows()