
import http.server
import socketserver
import json

from .url import *
from .sensors import Temperature
from .db import DB

database = None

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
            return

        body = self.rfile.read(content_length)

        # dispatch
        if endpoint == "temp":
            self.temp_handler(body)
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
    def _send_json_success(self):
        j = json.dumps({ "success": True })
        h = { "content-type": "application/json" }

        self._send(j, 200, h)

    # -------------------------------------------------------------------------
    def _send_json_error(self, e):
        j = json.dumps({ "success": False, "error": e })
        h = { "content-type": "application/json" }

        self._send(j, 200, h)
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
    def temp_handler(self, body):

        global database

        t = Temperature(body)
        try:
            t.validate()
        except ValidationError as v:
            self._send_json_error(str(v))

        database.connect()
        t.d['node'] = database.check_uuid(t.d['token'])
        if not t.d['node']:
            database.disconnect()
            self._send_error()
            return

        database.insert_temperature(t)
        database.disconnect()

        self._send_json_success()

# -------------------------------------------------------------------------
#
def run(config):

    # how could we do this without globals?
    global database 
    database = DB(config.db)
    database.init()

    with socketserver.TCPServer(("", config.port), Httpyd) as httpd:

        print("serving at port", config.port)
        httpd.serve_forever()
