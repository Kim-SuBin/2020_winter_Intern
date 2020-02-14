import keyboard
import numpy as np
import cv2
import time
import datetime

img = cv2.imread("./parkingLotImg/MoonParkingLot.png", cv2.IMREAD_COLOR)

parkingList = [(1180,303),(1180,269),(1180,244),(1180,218),(1180,183),
               (1180,156),(1180,129),(944,46),(919,46),(894,46),
               (870, 46),(836,46),(810,46)]
# parkingList[0]~[12]: a1~a13, [13]~[16]: b1~b4, [17]~[19]: c1~c3, [20]~[21]: d1~d2
# green = cv2.circle(img, parkingList[0], 7, (0, 255, 0), -1)
# red = cv2.circle(img, parkingList[0], 7, (0, 0, 255), -1)

carTable = [[0 for _ in range(4)] for _ in range(30)] # 차량 번호, 입차 시간, 출차 시간, 주차 구역
index = 0
count = 22

for i in range(len(parkingList)):
    cv2.circle(img, parkingList[i], 7, (0, 255, 0), -1)

while 1:
    cv2.imshow("show", img)
    k = cv2.waitKey(0)
    if k == 27:  # esc key
        break
    elif k == ord('i'):
        print("주차 가능 :", count, " /22")
        count -= 1
        carTable[index][0] = input("press incar: ")
        # 들어간 시간 입력
        now = datetime.datetime.now()
        carTable[index][1] = now.strftime('%Y-%m-%d %H:%M:%S')
        key = int(input("press key:")) # 구역
        # 구역 입력
        carTable[index][3] = key
        cv2.circle(img, parkingList[int(key) - 1], 7, (0, 0, 255), -1) # 색변경
        index += 1
    elif k == ord('o'):
        count += 1
        car = input("press outcar: ")
        for i in range(len(carTable)):
            if car == carTable[i][0]: # 나간 시간 입력
                now = datetime.datetime.now()
                carTable[i][2] = now.strftime('%Y-%m-%d %H:%M:%S')
        key = int(input("press key:"))
        cv2.circle(img, parkingList[int(key) - 1], 7, (0, 255,0), -1) # 색변경
        print("주차 가능 :", count, " /22")
        print(carTable)


cv2.destroyAllWindows()
