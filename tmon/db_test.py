import db

# build up database
# move into test folder
db = db.DB("example.sqlite3")

# init database

# create example uuid

db.connect()
db.check_uuid("asdfasdfasdf")
db.disconnect()

# remote database
