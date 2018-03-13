#Server side program for client server communication using TCP/IP protocol 
#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT1 = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT1))
s.listen(1)
conn, addr = s.accept()
print 'Connection address of 1:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    conn.send(data)
conn.close()
