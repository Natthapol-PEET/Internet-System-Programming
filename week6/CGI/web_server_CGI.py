from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler

serv = HTTPServer(("", 8080), CGIHTTPRequestHandler)
serv.serve_forever()