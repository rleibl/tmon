
import json

class BaseSensor():

    def __init__(self, json_in=None):
        """
        Constructor.
        If json is given, tries to construct the object using the json data
        given.
        """
        self.d = {
                "token": "",
                "type": "",
                "node": "",
                "time": "",
                "test": False,
                "data": {}
        }

        # XXX that doesn't look right.
        #     Perform correct validation of input
        #     Check for existence.
        if json_in != None:
            self.d = json.loads(json_in)

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
                self.d['data']['temperature'] 
                        = j['data']['temperature']
            except KeyError:
                print("Temperature data did not contain temperature field"


