from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import sys
import urlparse

import simplejson as json

class ReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = {}
        formats = {'json': 'application/json', 'text': 'text/plain'}
        request = urlparse.urlparse(self.path)

        try:
          (path, fmt) = request.path.split('.')
          if fmt not in formats.keys(): fmt = 'text'
        except ValueError:
          path = request.path
          if self.headers.get('accept', False) == 'application/json':
            fmt = 'json'
          else:
            fmt = 'text'

        module = path.split('/')[1]
        self.send_response(200)
        self.send_header('Content-Type', formats[fmt])
        self.end_headers()
        self.wfile.write("Some stuff - that needs to be formatted" + '\n')

def main():
    try:
        server = HTTPServer(('', 8080), ReqHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
