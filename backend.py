from flask import Flask, jsonify, request, make_response
app = Flask(__name__)

from middleware import is_user_exist, show_user, add_user, remove_user, authing

@app.route('/auth', methods=['POST'])
def lalaalla():
    if authing(request):
        return make_response(jsonify({"Info": "You are has been authed"}))
    else:
        return make_response(jsonify({"Info": "You are not permited_user"}), 403)


@app.route('/user/<who>', methods=['GET'])
def selector(who):
    answer = jsonify(show_user(who))
    if len(eval(answer.response[0])):
        return answer
    else:
        return make_response(jsonify({"Info": "user does not exist"}), 404)

@app.route('/user/add', methods=['POST'])
def inserter():
    body = request.get_json()
    print body
    return add_user(body)


@app.route('/user/delete', methods=['DELETE'])
def removerer():
    body = request.get_json()
    if not is_user_exist(body):
        return make_response(jsonify({"Info": "user does not exist"}), 400)
    else:
        remove_user(body)
        return make_response(jsonify({"Info": "user has been deleted"}), 200)

app.run(debug=True)
