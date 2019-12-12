#
# Create random temperature values in the range 23-26 and
# enter them into the sqlite database.
#

import sqlite3
import datetime
import random

database = "example.sqlite3"

conn = sqlite3.connect(database)
c = conn.cursor()

q = "INSERT INTO temperature VALUES (?, ?, ?)"

for h in range(100):
    node = "example"
    delta = datetime.timedelta(hours=h)
    time = datetime.datetime.now() - delta
    temp = random.randint(23000, 26000)

    c.execute(q, (node, time, temp))

conn.commit()

c.close()
conn.close()
