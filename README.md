## To start use this do next:
1. Create a new db;
```bash
sqlite3 /tmp/test.db < ./data_schema.sql
```
2. Start an API
```bash
python backend.py &
```


## examples:
check user:
```bash
curl -v http://127.0.0.1:5000/user/newlogin
```
to create a new user:
```bash
curl -v -XPOST http://127.0.0.1:5000/user/add -d '{"login": "newlogin", "name": "his name", "last_name": "his_surname"}' -H 'Content-type:application/json'
```

to delete a user:
```bash
curl -v -XDELETE http://127.0.0.1:5000/user/delete -d '{"login": "newlogin"} -H 'Content-type:application/json'
```
