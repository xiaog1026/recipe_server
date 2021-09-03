from flask import request
from flask_restx import Resource

from ..dto._user import UserDto
from ..service.user import save_new_user, get_all_users, get_a_user, registered_user, registered_visitor, change_account_password

api = UserDto.api
_user = UserDto.user
_new_user = UserDto.new_user
_new_registered_user = UserDto.new_registered_user

@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_users()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_new_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

@api.route('/update/user_id=<user_id>/account=<account>/password=<password>')
@api.param('user_id', 'user_id')
@api.param('account', 'account')
@api.param('password', 'password')
@api.response(404, 'change_username_password not found.')
class ChangeUserNamePassword(Resource):
    @api.doc('change user username and password')
    @api.marshal_list_with(_new_registered_user, envelope='data')
    def get(self, user_id, account, password):
        """ChangeUserNamePassword"""
        user = change_account_password(user_id, account, password)
        if not user:
            api.abort(404)
        else:
            return user

@api.route('/register/account=<account>/password=<password>')
@api.param('account', 'account')
@api.param('password', 'password')
@api.response(404, 'register_user not found.')
class RegisterUser(Resource):
    @api.doc('register user')
    @api.marshal_list_with(_new_registered_user, envelope='data')
    def get(self, account, password):
        """RegisterUser by account password"""
        user = registered_user(account, password)
        if not user:
            api.abort(404)
        else:
            return user

@api.route('/register')
@api.response(404, 'register_visitor not found.')
class RegisterVistor(Resource):
    @api.doc('register visitor')
    @api.marshal_list_with(_new_registered_user, envelope='data')
    def get(self):
        """RegisterVistor"""
        user = registered_visitor()
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/public_id=<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user by public id')
    @api.marshal_with(_user)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user