import sqlite3

class DB():

    def __init__(self, filename):
        self.sqlite3_filename = filename
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.sqlite3_filename)
        self.c = self.connection.cursor()

    def disconnect(self):
        self.c.close()
        self.connection.close()

    def check_uuid(self, uuid):
        """
        Check if a given uuid is valid.
        This does not create a uuid if requested. Use dbtool to create
        new uuids.
        """

        sql = 'SELECT node FROM tokens WHERE token=?'
        c.execute(sql, (uuid,))
        res = c.fetchone()
        if res != None:
            return True

        return False

    def insert_temperature(self, temp):

        sql = "INSERT INTO temperatures node, time, temp VALUES (?, ?, ?)"

        self.c.execute(sql, temp['node'],
                            temp['time'],
                            temp['data']['temperature'])

        self.c.commit()

