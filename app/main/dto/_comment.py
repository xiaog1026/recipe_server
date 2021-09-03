from flask_restx import Namespace, fields

class CommentDto:
    api = Namespace('comment', description='comment related operations')
    comment = api.model('comment', {
        'id': fields.Integer(required=True, description='comment id'),
        'comment': fields.String(required=True, description='comment content'),
        'comment_date': fields.DateTime(required=True, description='comment datetime'),
        'user_herf': fields.String(required=True, description='original user href'),
        'dish_id': fields.Integer(required=True, description='what dish comment'),
        'user_id': fields.Integer(required=True, description='who comment this'),
    })
    new_comment = api.model('new_comment', {
        'comment': fields.String(required=True, description='comment content'),
        'comment_date': fields.DateTime(required=True, description='comment datetime'),
        'user_herf': fields.String(required=True, description='original user href'),
        'dish_id': fields.Integer(required=True, description='what dish comment'),
        'user_id': fields.Integer(required=True, description='who comment this'),
    })