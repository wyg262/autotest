from socket import *
from time import ctime

host = ''
port = 21567
Buffsize = 1024
ADDR = (host, port)

server_sock_tcp = socket(AF_INET, SOCK_STREAM)
server_sock_tcp.bind(ADDR)
server_sock_tcp.listen(5)

while True:
	print("waitting for connect...")
	client_sock_tcp, addr = server_sock_tcp.accept()
	print("... connected from", addr)
	while True:
		data = client_sock_tcp.recv(Buffsize)
		if not data:
			break
		else:
			client_sock_tcp.send("%s, %s" %(ctime(), data))
	client_sock_tcp.close()
server_sock_tcp.close()
		
		
