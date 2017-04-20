import sqlite3

def do_select(who):
    db = sqlite3.connect('/tmp/test.db')
    query = "select * from rambler where login = \'{0}\';".format(who)
    cur = db.execute(query)
    return cur


#insert into rambler (login,first_name,last_name) values ("seege","sergey","sevostyanov");
def do_insert(user):
    db = sqlite3.connect('/tmp/test.db')
    query = "insert into rambler (login,first_name,last_name) values (\"{0}\", \"{1}\", \"{2}\");".format(user['login'],
                                                                                                    user['name'],
                                                                                                    user['last_name'])
    db.execute(query)
    db.commit()
    db.close()

