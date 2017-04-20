from flask import Flask, jsonify, Response, request, Request, make_response
app = Flask(__name__)
import sql3_connect as sql
from render import returner, convert_insert

myresponse = Response()

@app.route('/auth', methods=['GET'])
def authing():
    return 'Hello, World!'


@app.route('/user/<who>', methods=['GET'])
def selector(who):
    resp = sql.do_select(who)
    answer = jsonify(returner(resp))
    if len(answer.response[0]) == 0:
        return answer
    else:
        anwser = make_response(jsonify(returner(resp)), 404)
        return anwser

@app.route('/user/add', methods=['POST'])
def inserter():
    body = request.get_json()
    data = convert_insert(body)
    sql.do_insert(data)
    return make_response(jsonify({"Info": "user has been added"}), 200)

app.run(debug=True)
