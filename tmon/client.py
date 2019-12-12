#!/usr/bin/env python3

# globals
# -----------------------------------------------------------
temp_filename = ""
log_filename = ""
temp_server = ""

# logging
# -----------------------------------------------------------
def log(message):
    pass

# error handling
# -----------------------------------------------------------
class TemperatureException(Exception):
    pass


# read the temperature file
# -----------------------------------------------------------
def readtemp(filename):

    try:
        f = open(filename)
        l = f.readline() # throwaway
        if l == "":
            raise TemperatureException("Readline failed (1)")

        l = f.readline()
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

# http 
# -----------------------------------------------------------

# main
# -----------------------------------------------------------
t = readtemp("example.temp")
print(t)
