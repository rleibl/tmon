
from .context import tmon

import unittest

class TestClient(unittest.TestCase):

    def test_readtemp(self):
        c = tmon.Client()
        t = c.readtemp('test/example.temp')

        self.assertEqual(t, '20812')
        
