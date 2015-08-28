__author__ = 'Daeho'
from socketserver import ThreadingTCPServer, StreamRequestHandler

PQRT = 2000

class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        conn = self. request
        print('connection from', self.clinet_address)
        buf = conn.recv(1024)
        if not buf:
            print('nothing')

        else:
            print(buf)

server = ThreadingTCPServer(('127.0.0.1',2000),MyRequestHandler)
print('listening on park', PQRT)
server.serve_forever()
