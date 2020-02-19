import socket
import os
import time

UDP_IP = '222.107.177.42'
UDP_PORT = 6667

path = './img'
img_list = os.listdir(path)
img_list.sort()

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for file_name in img_list:
    clientSock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
    # print(file_name)
    data_transferred = 0
    with open('./img/' + file_name, 'rb') as f:
        print(file_name)
        try:
            data = f.read(1024)
            while data:
                data_transferred += clientSock.sendto(data, (UDP_IP, UDP_PORT))
                data = f.read(1024)
                time.sleep(0.0001)
                print("sleep")
        except Exception as e:
            print(e)
    clientSock.sendto('end'.encode(), (UDP_IP, UDP_PORT))
    print('end')

