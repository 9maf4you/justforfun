from time import time
from database import get_permission, update_auth_info, permited_user


def whoami(login):
    cursor = get_permission(login)
    for data in cursor:
        return data


def is_permitted(body_request):
    '''
        Tryes to checks ttl, ipaddress and authname that graps from body
        then access will be granted or forbidden
    '''
    perm = whoami(body_request.get('authname'))
    try:
        login, permission, authed, tstamp, ip = perm[0], perm[1], perm[2], perm[3], perm[4]
    except TypeError:
        return False

    if login in permited_user and time() - float(tstamp) < 90:
        return True
    else:
        return False

def auth_me(login, ip):
    update_auth_info(login, time(), ip)
    return True
