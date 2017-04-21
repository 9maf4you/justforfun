import database as sql
from security import auth_me, is_permitted
from flask import jsonify, make_response
from syslog import syslog


permited = sql.permited_user


def authing(request):
    try:
        login = request.get_json()['authname']
        REMOTE_ADDR = request.environ.get('REMOTE_ADDR')
        if login in permited:
            auth_me(login, REMOTE_ADDR)
            return True
        else:
            return False
    except IOError:
        return False


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
    if login:
        if [x for x in sql.do_select(login)]:
            return True
        else:
            return False


def add_user(body_request):
    ''' Graps authname from body and try to auth him
        also checks that user is not exist before do something
        It returns request object
        All magic makes here.
        if any problem has been occured it will be logged
    '''
    try:
        is_exist = is_user_exist(body_request)
        is_perm = is_permitted(body_request)
        if is_perm:
            if not is_exist:
                sql.do_insert(validate_req(body_request))
                return make_response(jsonify({"Info": "user has been added"}), 200)
            else:
                return make_response(jsonify({"Info": "user is exist"}), 400)
        elif not is_perm:
            return make_response(jsonify({"Info": "You are not permited"}), 403)
    except Exception as err:
        syslog(str(err))
        if isinstance(err, KeyError):
            return make_response(jsonify({"Error": "Bad request"}), 400)
        else:
            return make_response(jsonify({"Info": "Something went wrong"}), 500)


def show_user(user):
    users = dict()
    try:
        cursor = sql.do_select(user)
        for data in cursor:
            users.update({"login": {"name": data[1], "last_name": data[2]}})
        return users
    except Exception:
        return users


def remove_user(body_request):
    try:
        is_exist = is_user_exist(body_request)
        is_perm = is_permitted(body_request)
        if is_perm:
            if is_exist:
                sql.do_delete(body_request['login'])
                return make_response(jsonify({"Info": "user has been deleted"}), 200)
            else:
                return make_response(jsonify({"Info": "user does not exist"}), 400)
        elif not is_perm:
            return make_response(jsonify({"Info": "You are not permited"}), 403)
    except Exception as err:
        syslog(str(err))
        if isinstance(err, KeyError):
            return make_response(jsonify({"Error": "Bad request"}), 400)
        else:
            return make_response(jsonify({"Info": "Something went wrong"}), 500)
