To start use this do next:
1. Create a new db;
    sqlite3 /tmp/test.db < ./testdb.sql
2. Start an API
    python backend.py &
2. Do first request
    curl -v http://127.0.0.1:5000/user/9maf4you


examples:
    check user:
        curl -v http://127.0.0.1:5000/user/<username>
    create a new user:
        curl -v -XPOST http://127.0.0.1:5000/user/add -d '{"login": "newlogin", "name": "his name", "last_name": "his_surname"}' -H 'Content-type:application/json'
    delete a user:
        curl -v -XDELETE http://127.0.0.1:5000/user/delete -d '{"login": "newlogin"} -H 'Content-type:application/json'
