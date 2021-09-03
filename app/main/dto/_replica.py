from flask_restx import Namespace, fields

class ReplicaDto:
    api = Namespace('replica', description='replica related operations')
    replica = api.model('replica', {
        'id': fields.Integer(required=True, description='replica id'),
        'replica_href': fields.String(required=True, description='replica original href'),
        'replica_image_href': fields.String(required=True, description='replica original image href'),
        'comment': fields.String(required=True, description='author`s comment'),
        'dish_id': fields.Integer(required=True, description='what dish is copied'),
        'user_id': fields.Integer(required=True, description='what make the replica'),
    })
    new_replica = api.model('new_replica', {
        'replica_href': fields.String(required=True, description='replica original href'),
        'replica_image_href': fields.String(required=True, description='replica original image href'),
        'comment': fields.String(required=True, description='author`s comment'),
        'dish_id': fields.Integer(required=True, description='what dish is copied'),
        'user_id': fields.Integer(required=True, description='what make the replica'),
    })