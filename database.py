import sqlite3
dbname = '/tmp/test.db'
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

