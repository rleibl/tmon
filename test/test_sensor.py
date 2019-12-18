
from .context import tmon

import unittest

class SensorTest(unittest.TestCase):

    def test_temperature_sensor(self):
        j = '{"token": "", "data": {"temperature": ""}}'

        t = tmon.Temperature(j)
        self.assertRaises(tmon.errors.ValidationError, t.validate) # token not set

        j = '{"token": "asdfasdf", "data": {"temperature": ""}}'
        t = tmon.Temperature(j)
        self.assertRaises(tmon.errors.ValidationError, t.validate) # temperature not set


        j = '{"token": "asdfasdf", "data": {"temperature": "27000"}}'
        t = tmon.Temperature(j)
        try:
            t.validate() # temperature not set
        except:
            self.fail("Temperature.validate()")

