import sqlite3
import uuid
import os

from .log import log

class DB():

    def __init__(self, filename):
        self.sqlite3_filename = filename
        self.connection = None
        self.c = None # cursor placeholder

    def connect(self):
        self.connection = sqlite3.connect(self.sqlite3_filename)
        self.c = self.connection.cursor()

    def disconnect(self):
        self.c.close()
        self.connection.close()

    def init(self):

        if not os.path.exists(self.sqlite3_filename):
            log("Database file '{}' does not exist. Creating...".format(self.sqlite3_filename))
            self.connect() # this will create the file

            log("Creating table 'temperature'")
            sql = 'CREATE TABLE temperature (node VARCHAR(128), time DATE, temp INTEGER);'
            self.c.execute(sql)

            log("Creating table 'tokens'")
            sql = 'CREATE TABLE tokens (token VARCHAR(128), node  VARCHAR(128), desc  VARCHAR(256));'
            self.c.execute(sql)

            self.disconnect()
        else:
            # Database exists. Assume correct tables and everything.
            # Use dbtool.py to create (and possibly restore) a backup
            pass

    def add_uuid(self, node, desc=""):

        u = self.check_node(node)
        if u != None:
            return u

        u = str( uuid.uuid1() )
        u = u.replace('-', '')
        print("new uuid for node '{}': {}".format(node, u))

        sql = 'INSERT INTO tokens (token, node, desc) VALUES (?, ?, ?)'
        self.c.execute(sql, (u, node, desc))
        self.connection.commit()

        return u

    def check_node(self, node):
        sql = 'SELECT token FROM tokens WHERE node=?'
        self.c.execute(sql, (node,))
        res = self.c.fetchone()
        if res != None:
            return res[0]

        return None

    def check_uuid(self, uuid):
        """
        Check if a given uuid is valid.
        This does not create a uuid if requested. Use dbtool to create
        new uuids or add_uuid().
        """

        sql = 'SELECT node FROM tokens WHERE token=?'
        self.c.execute(sql, (uuid,))
        res = self.c.fetchone()
        if res != None:
            return True

        return False

    def insert_temperature(self, temp):
        """
        Expects a temperature class to write to the database
        """

        sql = "INSERT INTO temperatures (node, time, temp) VALUES (?, ?, ?)"

        self.c.execute(sql, temp['node'],
                            temp['time'],
                            temp['data']['temperature'])

        self.connection.commit()

