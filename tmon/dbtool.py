#!/usr/bin/env python3

import uuid
import sys

from .db import DB
from .config import Config

def print_help():
    print(
"""
    Helper tool for tmon.
    Usage:
        {} <command> [options]

    Where command is one of

    help
        Print this help

    get_token <node>
        Return the uuid for the given node. Create a new token for 
        node <node> and add it to the database it it does not exist.
    
""".format(sys.argv[0]))

def print_help_and_exit():
    print_help()
    sys.exit(-1)

def get_uuid(node):

    conf = Config()
    n = ""
    try:
        n = node[0]
    except IndexError:
        print("no node given after create_uuid command")
        print_help_and_exit()
        # TODO print all nodes and uuids

    db = DB(conf.db)
    db.connect()
    u = db.add_uuid(node) # will return existing uuid, if available
    db.disconnect()
    print(u)


# main
if __name__ == "__main__":
    command = ""
    try:
        command = sys.argv[1]
    except IndexError:
        print_help_and_exit()


    opts = sys.argv[2:]

    if command == "help":
        print_help_and_exit()
    elif command == "init_db":
        init_db()
    elif command == "get_uuid":
        get_uuid(opts)

    



