from flask import request
from flask_restx import Resource

from ..dto._comment import CommentDto
from ..service.comment import save_new_comment, get_all_comments, get_a_comment, get_all_comments_of_dish

api = CommentDto.api
_new_comment = CommentDto.new_comment
_comment = CommentDto.comment



@api.route('/')
class CommentList(Resource):
    @api.doc('list_of_registered_comments')
    @api.marshal_list_with(_comment, envelope='data')
    def get(self):
        """List all registered comments"""
        return get_all_comments()

    @api.response(201, 'Comment successfully created.')
    @api.doc('create a new comment')
    @api.expect(_new_comment, validate=True)
    def post(self):
        """Creates a new comment """
        data = request.json
        return save_new_comment(data=data)

@api.route('/dish_id=<dish_id>')
@api.param('dish_id', 'dish id')
@api.response(404, 'Comment not found.')
class CommentListInDish(Resource):
    @api.doc('get a dish by dish id')
    @api.marshal_list_with(_comment)
    def get(self, dish_id):
        """get all registered comments of a dish"""
        return get_all_comments_of_dish(dish_id)

@api.route('/dish_id=<dish_id>/user_id=<user_id>')
@api.param('dish_id', 'dish id')
@api.param('user_id', 'user id')
@api.response(404, 'Comment not found.')
class Comment(Resource):
    @api.doc('get a comment')
    @api.marshal_with(_comment)
    def get(self, dish_id, user_id):
        """get a comment given its identifier"""
        comment = get_a_comment(dish_id, user_id)
        if not comment:
            api.abort(404)
        else:
            return comment