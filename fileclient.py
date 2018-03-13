# client.py

import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.
data=raw_input()
s.connect((host, port))
s.send(data)

with open('received_file', 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = s.recv(1024)
        print data
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
s.close()

