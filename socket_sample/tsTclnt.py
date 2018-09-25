from socket import *


host = "localhost"
port = 21567
Buffsize = 1024
addr = (host, port)

clinet_sock_tcp = socket(AF_INET, SOCK_STREAM)
clinet_sock_tcp.connect(addr)

while True:
	data = raw_input('> ')
	if not data:
		break
	clinet_sock_tcp.send(data)
	data = clinet_sock_tcp.recv(Buffsize)
	if not data:
		break
	print data

clinet_sock_tcp.close()
