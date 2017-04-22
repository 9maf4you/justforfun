## To start use this do next:
1. Install requerements
```bash
pip install flask
```
2. Create a new db;
```bash
sqlite3 /tmp/test.db < ./data_schema.sql
```
3. Start an API
```bash
python backend.py &
```


## examples:
Firstable, you have to auth yourself, otherwise your won't to add ore delete user

auth:
```bash
curl -XPOST http://127.0.0.1:5000/auth -d '{"authname": "superturbo300"}' -H 'Content-Type: application/json'
```
check user:
```bash
curl -v http://127.0.0.1:5000/user/newlogin
```
to create a new user:
```bash
curl -v -XPOST http://127.0.0.1:5000/user/add -d '{"authname": "superturbo300", "login": "newlogin", "name": "MAxs", "last_name":"dsadasd"}' -H 'Content-Type: application/json'
```
check if user has been created:
```bash
curl -v http://127.0.0.1:5000/user/newlogin
```
to delete a user:
```bash
curl -v -XDELETE http://127.0.0.1:5000/user/delete -d '{"authname": "superturbo300", "login": "newlogin"}' -H 'Content-Type: application/json'
```


## TODO
what has to be improved:
1. There are a lot of duplicate code in the database.py. It might be improved by adding a wrapper
2. Also when it checks user somewhere sometimes it makes more then one query to db
3. Authing has to be more powerful and flexible

