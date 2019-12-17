
class Client():

    # init
    # -----------------------------------------------------------
    def __init__(self, port=1337, host=None, filename=None):
        self.filename = filename
        self.host     = host
        self.port     = port

    # try finding sensor files
    # -----------------------------------------------------------
    def autodiscover(self):
        pass

    # send the temperature to the server
    # -----------------------------------------------------------
    def send(self, temperature):




    # read the temperature file
    # -----------------------------------------------------------
    def readtemp(self, filename=None):

        if not filename and not self.filename:
            raise ConfigException("Filename not set")

        try:
            f = open(filename)
            l = f.readline() # throwaway
            if l == "":
                f.close()
                raise TemperatureException("Readline failed (1)")

            l = f.readline()
            f.close()
            if l == "":
                raise TemperatureException("Readline failed (2)")

            try:
                i = l.index('=')
            except ValueError:
                raise TemperatureException("File corrupt:" + l)

            temperature = l[ i+1 : -1]

            return temperature

        except Exception as e:
                raise TemperatureException("File open failed:" + e)

