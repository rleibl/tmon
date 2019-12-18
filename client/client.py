from http.client import HTTPConnection
import json
import datetime

port     = 13117
temphost = "localhost"
filename = '../test/example.temp'
token    = 'c791daaa211911ea845c3c15c2d309e2'
logfile  = 'client.log'

def log_and_exit(message):
    with open(logfile, "a") as f:
        f.write(message)
        sys.exit(0)

# read the temperature file
# -----------------------------------------------------------
try:
    f = open(filename)
    l = f.readline() # throwaway
    if l == "":
        f.close()
        log_and_exit("Readline failed (1)")

    l = f.readline()
    f.close()
    if l == "":
        log_and_exit("Readline failed (2)")

    try:
        i = l.index('=')
    except ValueError:
        log_and_exit("File corrupt:" + l)

    temperature = l[ i+1 : -1]


except Exception as e:
        log_and_exit("File open failed:" + e)

obj = {
    "type": "temperature",
    #"time": datetime.datetime.now(), # not json serializable
    "token": token,
    "data": {
        "temperature": temperature
    }
}

# send the temperature to the server
# -----------------------------------------------------------
con = HTTPConnection(temphost, port)

headers = {"Content-Type": "application/json"}

body = json.dumps(obj)
print(body)
con.request("POST", "/temp", body, headers)
r = con.getresponse()
print(r.status, r.reason)
