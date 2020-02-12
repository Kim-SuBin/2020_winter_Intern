import socket
import threading
import time
import udp_server

class UDPServerMultiClient(udp_server.UDPServer):
	def __init__(self, host, port):
		super().__init__(host, port)
		self.socket_lock = threading.Lock() # Use a lock to make sure only one thread uses the sento() method at a time.
	
	def handle_request(self, title, addr):
		# Handle client
		count = 0
		def s():
			count += 1
			while True:	
				data_transferred = 0
				print ("Messsage: ", title)
				if not self.title:
					print("Error")
				else :
					print("else")
					data, addr = serverSock.recvfrom(1024)
					with open('./img/'+ title +".JPG", 'wb') as f:
						try:
							while data:
								f.write(data)
								data_transferred += len(data)
								data, addr = serverSock.recvfrom(1024)
								if data == b'end':
									self.print('end')
									s()
							self.print("while end")
						except Exception as e:
							self.print(e)
	
	def wait_for_client(self):
		# Wait for clients and handle their requests
		try:
			while True:
				try:
					title, client_address = self.sock.recvfrom(1024)
					c_thread = threading.Thread(target = self.handle_request, args = (data, client_address))
					c_thread.daemon = True
					c_thread.start()
				except Exception as e:
					self.printwt(e)
		except KeyboardInterrupt:
			self.shutdown_server()

def main():
	# Create a UDP Server and handle multiple clients simultaneously
	udp_server = UDPServerMultiClient('222.107.177.42', 6667)
	udp_server.configure_server()
	udp_server.wait_for_client()

if __name__ == '__main__':
	main()
