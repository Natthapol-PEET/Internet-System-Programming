#!/usr/bin/env python

import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect(("www.google.com" , 80))
    # s.sendall(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")
    s.sendall(b"GET / HTTP/1.1\r\n\r\n")
    print(str(s.recv(1024), 'utf-8'))