#!/usr/bin/python3           # This is server.py file
import socket                                         

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
serversocket.bind((host, port))                                  

# queue up to 5 requests
serversocket.listen(5)                                           

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()      

   # print ip address
   print("Got a connection from %s" % str(addr))
    
   # Send data to client
   msg = 'What\'s your name ?' + "\r\n"
   clientsocket.send(msg.encode('ascii'))

   # Recive message from client
   data = clientsocket.recv(1024)

   # Send data to client
   msg = '\r\nHello ' + str(data.decode()) + "\r\n"
   clientsocket.send(msg.encode())

   clientsocket.close()
