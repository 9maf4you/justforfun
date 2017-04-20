import database as sql
from security import auth_me
from time import sleep, time

for s in xrange(0, 2):
    try:
        permited = [x[0] for x in sql.permited_list()]
        break
    except Exception:
        sleep(s)


def authing(request):
    try:
        from pprint import pprint
        print request.get_json()#['environ']['REMOTE_ADDR']
        login = request.get_json()['login']
        REMOTE_ADDR = request.environ.get('REMOTE_ADDR')
        if login in permited:
            auth_me(login, REMOTE_ADDR)
            return True
        else:
            return False
    except IOError:
        return False


def convert_insert(data):
    values = ['login', 'name', 'last_name']
    ret = dict()
    try:
        for vals in values:
            ret[vals] = data[vals]
    except Exception:
        pass
    return ret


def validate_req(data):
    values = ['login', 'name', 'last_name']
    ret = dict()
    try:
        for vals in values:
            ret[vals] = data[vals]
    except Exception:
        pass
    return ret


def is_user_exist(data):
    login = validate_req(data).get('login')
    if login:
        if [ x for x in sql.do_select(login)]:
            return True
        else:
            return False

def add_user(data):
    try:
        sql.do_insert(convert_insert(data))
        return True
    except Exception:
        return False

def show_user(user):
    users = dict()
    try:
        cursor = sql.do_select(user)
        for data in cursor:
            users.update({"login": {"name": data[1], "last_name": data[2]}})
        return users
    except Exception:
        return users


def remove_user(data):
    try:
        login = data['login']
        sql.do_delete(login)
        return True
    except Exception:
        return False
