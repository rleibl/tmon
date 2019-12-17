
import urllib.parse

class Url():

    def __init__(self):
        self.path = []
        self.params = {} # parameters are unordered


def urlparse(url):
    u = Url()
    o = urllib.parse.urlparse(url)

    if o.path == "" or o.path == "/":
        u.path = ['/']
    else:
        p = o.path.rstrip("/")
        p = p.lstrip("/")

        u.path = p.split('/')

    q = urllib.parse.parse_qs(o.query)
    for k, v in q.items():
        u.params[k] = v[0]

    return u


