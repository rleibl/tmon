
from .context import tmon

import unittest

class SensorTest(unittest.Testcase):

    def test_temperature_sensor(self):
        json = '{"token": "", "type": "", "time": "", "test": false, "data": {"temperature": ""}}'
