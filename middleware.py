import database as sql

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
    print login
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
