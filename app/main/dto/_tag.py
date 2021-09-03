from flask_restx import Namespace, fields

class TagDto:
    api = Namespace('tag', description='tag related operations')
    tag = api.model('tag', {
        'id': fields.Integer(required=True, description='tag id'),
        'tagname': fields.String(required=True, description='tag name'),
    })
    new_tag = api.model('new_tag', {
        'tagname': fields.String(required=True, description='tag name'),
    })