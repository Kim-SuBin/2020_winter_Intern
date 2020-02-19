import socket
import yolo_object_detection

UDP_IP = '222.107.177.42'
UDP_PORT = 6668

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP, UDP_PORT))
detection = yolo_object_detection.DETECT()

while True:
    data, addr = serverSock.recvfrom(1024)
    print(data)
    if data == b'start':        
        parkingList = detection.main()
        message = ''
        for i in parkingList:
            message += str(i)
        serverSock.sendto(message.encode(), addr)
