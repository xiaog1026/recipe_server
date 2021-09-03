from flask import request
from flask_restx import Resource

from ..dto._tag import TagDto
from ..service.tag import *

api = TagDto.api
_tag = TagDto.tag
_new_tag = TagDto.new_tag


@api.route('/')
class TagList(Resource):
    @api.doc('list up all tags')
    @api.marshal_list_with(_tag, envelope='data')
    def get(self):
        """List all registered users"""
        return get_tags()

    @api.response(201, 'Tag successfully created.')
    @api.doc('create a new tag')
    @api.expect(_new_tag, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_tag(data=data)


@api.route('/tagname=<tagname>')
@api.param('tagname', 'tag name')
@api.response(404, 'Tag not found.')
class Tag(Resource):
    @api.doc('get a tag by name')
    @api.marshal_with(_tag)
    def get(self, tagname):
        """get a user given its identifier"""
        tag = get_a_tag_by_name(tagname)
        if not tag:
            api.abort(404)
        else:
            return tag