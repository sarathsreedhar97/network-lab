#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while 1:
           MESSAGE = raw_input("User1: ");
	   if MESSAGE == "exit":
		s.send(MESSAGE);
		break;
           s.send(MESSAGE)
           data = s.recv(BUFFER_SIZE)
	   print "User2:" , data
s.close()

