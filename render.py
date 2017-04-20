import sqlite3 as sql
from flask import Response


def returner(cursor):
    users = dict()
    for data in cursor:
        users.update({ "login": {"name": data[1], "last_name": data[2] }})
    return users


def convert_insert(data):
    values = ['login', 'name', 'last_name']
    ret = dict()
    try:
        for vals in values:
            ret[vals] = data[vals]
    except Exception:
        pass
    return ret
