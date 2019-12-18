
from .context import tmon

import unittest
import os

# globals
db_file = "test/test.sqlite3"

class DBTest(unittest.TestCase):

    def setUp(self):
        # build up database
        self.db = tmon.DB(db_file)
        
        # init database
        self.db.init()

    def tearDown(self):

        if os.path.exists(db_file):
            os.remove(db_file)

    def test_uuid(self):

        self.db.connect()

        u = self.db.add_uuid("example")
        self.assertTrue(self.db.check_uuid(u))

        u2 = self.db.check_node("example")
        self.assertEqual(u, u2)

        u2 = self.db.add_uuid("example")
        self.assertEqual(u, u2)

        self.assertFalse(self.db.check_uuid('somerandom'))

        self.db.disconnect()

