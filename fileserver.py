# server.py

import socket                   # Import socket module
from multiprocessing import Process
import os
port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'


conn, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
data = conn.recv(1024)
print('Server received', repr(data))
filename='data.txt'
id=os.getpid()
f = open(filename,'rb')
l = f.read(1024)
while (l):
       	conn.send(l)
   	l = f.read(1024)
f.close()
conn.send("process id " +str(os.getpid()))
print('Done sending')
conn.close()
