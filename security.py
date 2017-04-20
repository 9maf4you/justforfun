from datetime import datetime
from time import time
from database import get_permission, update_auth_info, drop_auth

'''
def whoami(login):
    cursor = get_permission(login)
    for data in cursor:
        return data
'''

def is_permitted(login):
    data = whoami(login)
    login, permission, authed, tstamp = data[0], data[1], data[2], data[3]
    if login in permited and time() - tstamp < 30:
        return True
    else:
        return False


def can_i(login):
    pass

def auth_me(login, ip):
    update_auth_info(login, time(), ip)
    return True
