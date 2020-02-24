import pandas as pd
import datetime
import time
import pygame
from pygame import *
from pygame.locals import *
import numpy
import socket


UDP_IP = '222.107.177.42'
UDP_PORT = 6668
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

parkingList = [(1180,303), (1180,269), (1180,244), (1180,218), (1180,183),(1180,156),(1180,129),(944,46),(919,46),(894,46),
               (870, 46),(836,46) ,(810,46), (747,46), (720,46), (695,46), (660,46), (633,46), (573,46), (548,46),
               (517,46), (486,46), (458,46), (396,46), (370,46), (344,46), (288,46), (257,46), (222,46), (203,46),
               (175,46),(149,46), (76,46), (34,126), (34,148), (34,172), (34,198), (34,222), (34,248),(34,273),
               (34,297), (34,323), (34,347), (34,372), (34,397), (93,440), (114,440), (149,440), (176,440),(199,440),
               (223,440), (258,440), (280,440), (309,440), (345,440), (370,440), (397,440), (434,440), (457,440),(520,440),
               (545,440), (575,440), (605,440), (633,440), (661,440), (694,440), (719,440), (747,440), (780,440),(807,440),
               (835,440), (875,440), (901,440), (928,440), (953,440), (1000,440), (1026,440), (1051,440), (1085,440),(1107,440),
               (1127,440), (1061,166), (1036,166), (1011,166), (985,166), (962,166), (937,166), (914,166), (887,166),(835,166),
               (809,166), (785,166), (761,166), (736,166), (710,166), (686,166), (700, 240), (700, 270),(689,323),(712,323),
               (741,323), (766,323), (797,323), (822,323), (849,323), (878,323), (898,323), (956,323), (984,323),(1009,323),
               (1062,323), (582,166), (558,166), (533,166), (505,166), (483,166), (434,166), (412,166), (390,166),(364,166),
               (339,166), (315,166), (290,166), (265,166), (238,166), (214,166), (188,166), (164,166), (139,166),(145,223),
               (145,241), (145,264), (138,323), (164,323), (186,323), (210,323), (242,323), (264,323), (314,323),(338,323),
               (358,323), (382,323), (408,323), (429,323), (458,323), (479,323), (507,323), (529,323), (555,323),(580,323),
               (565,240), (565,270)]

screen = pygame.display.set_mode((1332,477), pygame.DOUBLEBUF)

class PROCESSING:
    def main(self):
        pygame.init()
        img = pygame.image.load("./parkingLotImg/MoonParkingLot.png")
        img = pygame.transform.scale(img, (1332, 477))
        screen.blit(img, (0, 0))
        for i in range(len(parkingList)):
            pygame.draw.circle(screen, (0, 255, 0), parkingList[i], 5)
        pygame.display.flip()
        carTable = [] # 주차 구역, 입차 시간, 출차 시간
        carArray = numpy.array(carTable)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_ESCAPE): running = False
                pygame.display.flip()
                clientSock.sendto("start".encode(), (UDP_IP, UDP_PORT))
                data, addr = clientSock.recvfrom(1024)
                yolo_detection = data.decode() # yolo result
                yolo_detection = [int(i) for i in yolo_detection]
                check = [0] * len(yolo_detection) # in, not in check
                print("주차 가능:", len(parkingList) - sum(yolo_detection), "/", len(parkingList))

                for i in range(len(yolo_detection)):
                    carArray = numpy.array(carTable)
                    if yolo_detection[i]:
                        if len(carTable) == 0:
                            check[i] = 1
                        else:
                            for j in range(len(carTable)):
                                carArray = numpy.array(carTable)
                                if str(i) not in carArray[:, 0]:
                                    check[i] = 1
                                elif carArray[:, 0][j] == str(i) and carArray[:, 2][j] == str(0):
                                    check[i] = 0
                                elif carArray[:, 0][j] == str(i) and carArray[:, 2][j] != str(0):
                                    check[i] = 1
                    else:
                        for j in range(len(carTable)):
                            if carTable[j][0] == i and carTable[j][2] == 0:
                                now = datetime.datetime.now()
                                carTable[j][2] = now.strftime('%Y-%m-%d %H:%M:%S')
                        pygame.draw.circle(screen, (0,255,0), parkingList[i], 5)
                        # cv2.circle(img, parkingList[i], 5, (0, 255, 0), -1)  # Create green circle
                for i in range(len(check)):
                    if check[i]:
                        now = datetime.datetime.now()
                        carTable.append([i, now.strftime('%Y-%m-%d %H:%M:%S'), 0])
                df = pd.DataFrame(carTable, columns=['주차구역', '입차', '출차'])
                print(df)
        pygame.quit()

if __name__ == '__main__':
    processing = PROCESSING()
    processing.main()
