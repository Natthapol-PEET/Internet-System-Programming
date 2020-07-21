#!/usr/bin/python3           # This is client.py file

import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect((host, port))                               

# Receive no more than 1024 bytes ('What\'s your name ?')
msg = s.recv(1024)                                     
print (msg.decode('ascii'))

# Enter name and send data to server
data = str(input(''))
s.send(data.encode())

# Receive no more than 1024 bytes ('Hello __name__')
msg = s.recv(1024)
print(msg.decode())

s.close()

