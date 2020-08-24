from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200, "OK")
            self.send_header('Content-type','text/plain')
            self.end_headers()
            self.wfile.write(("""<html>
                <head><title> Hello </title></head>
                <body> Hello, World!! </body> 
            </html>""").encode())


serv = HTTPServer(("localhost", 8080), HelloHandler)
serv.serve_forever()