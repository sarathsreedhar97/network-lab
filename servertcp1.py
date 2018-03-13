                                                                          

#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT1 = 5005
TCP_PORT2 = 5006
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT1))
s.listen(1)

p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
p.bind((TCP_IP, TCP_PORT2))
p.listen(1)

conn, addr = s.accept()
conn1, addr1= p.accept()
print 'Connection address of 1:', addr
print 'Connection address of 2:', addr1
while 1:
    data = conn.recv(BUFFER_SIZE)
    conn1.send(data)
    data1= conn1.recv(BUFFER_SIZE)
    conn.send(data1)
conn.close()
conn1.close()
