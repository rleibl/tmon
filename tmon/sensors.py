
import json

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

        if json_in != None:
            j = json.loads(json_in)
            try:
                self.d['data']['temperature'] = j['data']['temperature']
            except KeyError:
                print("Temperature data did not contain temperature field")

