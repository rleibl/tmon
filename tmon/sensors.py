
import json
import datetime

from .errors import *

MIN_TEMP = -192

class BaseSensor():

    def __init__(self, json_in=None):
        """
        Constructor.
        If json is given, tries to construct the object using the json data
        given.
        """
        j = {}
        if json_in != None:
            j = json.loads(json_in)

        self.d = {}
        self.d["token"] = j.get("token", "")
        self.d["type"]  = j.get("type", "")
        self.d["node"]  = j.get("node", "")
        self.d["time"]  = j.get("time", "")
        self.d["test"]  = j.get("test", False)
        self.d["data"]  = {}
        
    def validate(self):
        if self.d["token"] == "":
            raise ValidationError("token not set")

        # type is currently not really important. 
        # There is only temperature, and it is managed by the /temp endpoint
        #self.d["type"]

        # XXX if node is not set, we could look it up in the database
        #self.d["node"]

        # if time is not set, use current server time
        if self.d["time"] == "":
            self.d["time"] = datetime.datetime.now()

        # ignore test here
        #self.d["test"]

    def print(self):
        print("    'token': '{}'".format(self.d['token']))
        print("    'type':  '{}'".format(self.d['type']))
        print("    'node':  '{}'".format(self.d['node']))
        print("    'time':  '{}'".format(self.d['time']))
        print("    'test':  '{}'".format(self.d['test']))


    def to_json(self):
        """
        Return this object as json string.
        """
        s = json.dumps(self.d)
        return s


class Temperature(BaseSensor):
    
    def __init__(self, json_in=None):
        """
        Call base constructor
        Adds data field
            'temperature'
        """
        BaseSensor.__init__(self, json_in)
        
        self.d['data']['temperature'] = ""

        j = {}
        if json_in != None:
            j = json.loads(json_in)

        self.d['data']['temperature'] = j.get('data', {}).get('temperature', MIN_TEMP)

    def validate(self):
        BaseSensor.validate(self)
    
        t = self.d['data']['temperature']
        if t == MIN_TEMP or t == "":
            raise ValidationError("No temperature given")

    def print(self):
        
        print("{")
        BaseSensor.print(self)
        print("    'data': {")
        print("        'temperature': '{}'".format(self.d['data']['temperature']))
        print("    }")
        print("}")



