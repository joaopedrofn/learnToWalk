import http.server
import socketserver

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        self.wfile.write('{"teste": "ok"}'.encode('utf8'))
        return

httpd = socketserver.TCPServer(('', PORT), Handler)

print("Listening port ", PORT)
httpd.serve_forever()