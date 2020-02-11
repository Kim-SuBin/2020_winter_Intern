import socket

UDP_IP = '222.107.177.42'
UDP_PORT = 6667

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP, UDP_PORT))

def s():
	while True:	
		data_transferred = 0
		title, addr = serverSock.recvfrom(1024)
		print ("Messsage: ", title)
		if not title:
			print("Error")
		else :
			print("else")
			data, addr = serverSock.recvfrom(1024)
			with open('./img/'+ title.decode(), 'wb') as f:
				try:
					while data:
						f.write(data)
						data_transferred += len(data)
						data, addr = serverSock.recvfrom(1024)
						if data == b'end':
							print('end')
							s()
					print("while end")
				except Exception as e:
					print(e)

s()
