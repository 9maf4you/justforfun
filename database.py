import sqlite3
dbname = '/tmp/test.db'

# TODO need a decorator here

def do_select(who):
    db = sqlite3.connect(dbname)
    query = "select * from company where login = \'{0}\';".format(who)
    cur = db.execute(query)
    return cur


def do_insert(user):
    db = sqlite3.connect(dbname)
    query = "insert into company (login,first_name,last_name) values (\"{0}\", \"{1}\", \"{2}\");".format(user['login'],
                                                                                                    user['name'],
                                                                                                    user['last_name'])
    db.execute(query)
    db.commit()
    db.close()

def do_delete(user):
    db = sqlite3.connect(dbname)
    query = "DELETE FROM company WHERE login = \"{0}\"".format(user)
    db.execute(query)
    db.commit()
    db.close()

def get_permission(login):
    db = sqlite3.connect(dbname)
    query = "select * from permission where login = \'{0}\';".format(login)
    db.execute(query)
    db.close()

def permited_list():
    db = sqlite3.connect(dbname)
    query = "select login from permission;"
    cur = db.execute(query)
    return cur

def drop_auth(login):
    db = sqlite3.connect(dbname)
    query = "update permission set authed = 0 where login = \'{0}\';".format(login)
    db.execute(query)
    db.close()

def update_auth_info(login, ts):
    db = sqlite3.connect(dbname)
    print ts
    query = "update permission set authed = 1, timestmp = {0} where login = \'{1}\';".format(ts, login)
    print query
    db.execute(query)
    db.commit()
    db.close()
