from datetime import datetime
from time import time
from database import get_permission, update_auth_info, drop_auth

def whoami(login):
    cursor = get_permission(login)
    for data in cursor:
        return data


def can_i(login):
    data = whoami(login)
    login, permission, authed, tstamp = data[0], data[1], data[2], data[3]
    if time() - tstamp < 30:
        drop_auth(login)
        return False
    else:
        return True

def auth_me(login):
    print time()
    update_auth_info(login, time())
    return True
