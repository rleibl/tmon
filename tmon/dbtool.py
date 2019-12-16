#!/usr/bin/env python3

import uuid
import sys

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

    init_db
        Initialize the database // TODO
    
""".format(sys.argv[0]))

def print_help_and_exit():
    print_help()
    sys.exit(-1)

def get_uuid(node):
    n = ""
    try:
        n = node[0]
    except IndexError:
        print("no node given after create_uuid command")
        print_help_and_exit()
        # TODO print all nodes and uuids

    # TODO Check for uuid

    u = str( uuid.uuid1() )
    u = u.replace('-', '')
    print("uuid for node '{}'".format(n))
    print(u)

    # TODO insert into database
    #      check if uuid exists for node

def insert_uuid(node, uuid):
    pass


def init_db():
    # TODO read config
    # TODO check if file exists
    # TODO check if tables exist
    # TODO create tables
    pass

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

    



