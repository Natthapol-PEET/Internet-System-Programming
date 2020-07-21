from socket import socket

s = socket()

s.connect(('www.youtube.com', 80))

s.send('GET / HTTP/1.0\n\n'.encode())

data = s.recv(10000)
print(data.decode())

s.close()