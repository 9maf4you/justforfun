import sqlite3
from time import sleep
dbname = '/tmp/test.db'


def connect_to_db(func):
    def wrapper(arg):
        db = sqlite3.connect(dbname)
        query = func(arg)
        cur = db.execute(query)
        db.commit()
        return cur
    return wrapper


@connect_to_db
def do_select(who):
    return "select * from company where login = \'{0}\';".format(who)


@connect_to_db
def do_insert(user):
    query = "insert into company (login,first_name,last_name) values (\"{0}\", \"{1}\", \"{2}\");".format(user['login'],
                                                                                                    user['name'],
                                                                                                    user['last_name'])
    return query


@connect_to_db
def do_delete(user):
    return "DELETE FROM company WHERE login = \"{0}\"".format(user)


@connect_to_db
def get_permission(login):
    return "select * from permission where login = \'{0}\';".format(login)


def permited_list():
    db = sqlite3.connect(dbname)
    query = "select login from permission;"
    cur = db.execute(query)
    return cur


def update_auth_info(login, ts, ip):
    db = sqlite3.connect(dbname)
    query = "update permission set authed = 1, timestmp = {0}, ip = \'{1}\' where login = \'{2}\';".format(ts, ip, login)
    db.execute(query)
    db.commit()
    db.close()


for s in xrange(0, 2):
    try:
        permited_user = [x[0] for x in permited_list()]
        break
    except Exception:
        sleep(s)
