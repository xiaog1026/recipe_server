from flask_restx import Namespace, fields

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'id': fields.Integer(required=True, description='user id'),
        'public_id': fields.String(required=True, description='user id from crawled data'),
        'username': fields.String(required=True, description='user username'),
        'registered_on': fields.DateTime(required=True, description='the datetime resistered on'),
    })

    new_user = api.model('new_user', {
        'public_id': fields.String(required=True, description='user id from crawled data'),
        'username': fields.String(required=True, description='user username'),
        'registered_on': fields.DateTime(required=True, description='the datetime resistered on'),
    })

    new_registered_user = api.model('registered_user', {
        'id': fields.String(required=True, description='user id from crawled data'),
    })