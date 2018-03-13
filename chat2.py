#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5006
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
	   data = s.recv(BUFFER_SIZE)
           print "User1:" , data
           MESSAGE = raw_input("User2: ");
	   if MESSAGE == "exit":
		s.send(MESSAGE);
		break;
           s.send(MESSAGE)
s.close()




