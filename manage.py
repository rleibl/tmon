
from tmon.config import Config
from tmon.db import DB
import tmon.server


import uuid
import sys

def print_help():
    print(
"""
    Manage tool for tmon.
    Usage:
        {} <command> [options]

    Where command is one of

    run
        run the server

    help
        Print this help

    get_token <node>
        Return the uuid for the given node. Create a new token for 
        node <node> and add it to the database it it does not exist.

    list
        List all nodes and tokens
    
""".format(sys.argv[0]))

def print_help_and_exit():
    print_help()
    sys.exit(-1)

def get_token(node):

    conf = Config()
    n = ""
    try:
        n = node[0]
    except IndexError:
        print("no node given after get_token command")
        print_help_and_exit()
        # TODO print all nodes and tokens

    db = DB(conf.db)
    db.connect()
    u = db.add_uuid(n) # will return existing uuid, if available
    db.disconnect()
    print("{}: {}".format(node, u))

def list_nodes():
    conf = Config()
    db = DB(conf.db)
    db.connect()
    result = db.list_nodes()
    db.disconnect()

    for i in result:
        print("{}: {}".format(i['node'], i['token']))

def run():
    c = Config()
    tmon.server.run(c)

    db = DB(conf.db)
    db.connect()
    u = db.add_uuid(n) # will return existing uuid, if available
    db.disconnect()
    print("{}: {}".format(node, u))

# main
if __name__ == "__main__":
    command = ""
    try:
        command = sys.argv[1]
    except IndexError:
        print_help_and_exit()


    opts = sys.argv[2:]

    if command == "get_token":
        get_token(opts)
    elif command == "run":
        run()
    elif command == "list":
        list_nodes()
    else:
        print_help_and_exit()


    



