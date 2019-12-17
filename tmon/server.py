
import http.server
import socketserver
import json

from .url import *

class Httpyd(http.server.SimpleHTTPRequestHandler):

    # -------------------------------------------------------------------------
    #
    def do_POST(self):
        """
        POST request dispatcher.
        """
        print("POST {}".format(self.path))

        u = urlparse(self.path)
        endpoint = u.path[0]

        content_length = int(self.headers['Content-Length'])
        if not content_length:
            self._send_error("Bad Request", 400)

        body = self.rfile.read(content_length)

        # dispatch
        if endpoint == "jsontest":
            self.jsontest_handler(body)
        else:
            self.default_handler()

    # -------------------------------------------------------------------------
    #
    def do_GET(self):
        """
        GET request dispatcher.
        """

        u = urlparse(self.path)
        endpoint = u.path[0]
        
        # dispatch
        if endpoint == 'test':
            self.test_handler()
        else:
            self._send_error("Not Found", 404)


    # -------------------------------------------------------------------------
    #
    def _send_error(self, message = "Bad Request", code=400):

        e = """
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>{} {}</title>
</head><body>
<h1>{}</h1>
</body></html>
""".format(code, message, message)

        self._send(message=e, code=code)

    # -------------------------------------------------------------------------
    #
    def _send(self, message="<html><body>no</body></html>", 
                    code=200,
                    headers={}):
        """
        Assemble return message and send to the client.
      
        The default Content-Type header is "text/html" and may be overwritten
        by the given headers. 
     
        The Content-Length header is calculated automatically
        """

        self.send_response(code)

        b = str.encode(message)
        self.send_header("Content-Length", len(b))

        # Content-Type may be overwritten by given headers
        self.send_header("Content-Type", "text/html")
        for h, v in headers.items():
            self.send_header(h, v)
        self.end_headers()

        self.wfile.write(b)

    # -------------------------------------------------------------------------
    # Handler functions
    # -------------------------------------------------------------------------

    # -------------------------------------------------------------------------
    #
    def default_handler(self):
        """
        Calls _send without parametes causing the default answer to be sent
        to the client
        """
        self._send() # default

    # -------------------------------------------------------------------------
    #
    def test_handler(self):
        message = """
        <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
        <html><head>
        <title>It works</title>
        </head><body>
        <h1>It works</h1>
        </body></html>
        """
        self._send(message)

    # -------------------------------------------------------------------------
    #
    def jsontest_handler(self, data):
        try:
            struct = json.loads(data)
        except json.JSONDecodeError:
            self._send_error("Bad Request", 400)
            return

        print("jsontest: ", struct)
        j = json.dumps(struct)
        header = {'Content-Type': 'application/json'}
        self._send(j, 200, header)

# -------------------------------------------------------------------------
#
def run(port):

    with socketserver.TCPServer(("", port), Httpyd) as httpd:
        print("serving at port", port)
        httpd.serve_forever()
