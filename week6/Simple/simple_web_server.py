from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import os

os.chdir("D:\ปี 4 เทอม 1\Internet System Programming\week6\Simple")

serv = HTTPServer(("localhost", 8080), SimpleHTTPRequestHandler)
serv.serve_forever()