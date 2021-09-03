from flask import request
from flask_restx import Resource

from ..dto._dish import DishDto
from ..service.dish import *
from ..service import tag as tag_service

api = DishDto.api
_dish_summary = DishDto.dish
_new_dish_summary = DishDto.new_dish
_dish_detail = DishDto.dish_detail

@api.route('/')
class DishList(Resource):
    @api.doc('list_of_registered_dishs')
    @api.marshal_list_with(_dish_summary, envelope='data')
    def get(self):
        """List up registered dish"""
        return get_dish_summary()

    @api.response(201, 'Dish successfully created.')
    @api.doc('create a new dish')
    @api.expect(_new_dish_summary, validate=True)
    def post(self):
        """Creates a new dish """
        data = request.json
        return save_new_dish(data=data)

@api.route('/public_id=<dish_public_id>')
@api.param('dish_public_id', 'dish original id')
@api.response(404, 'Dish not found.')
class DishSummary(Resource):
    @api.doc('get a dish by public id')
    @api.marshal_with(_dish_summary)
    def get(self, dish_public_id):
        """get a dish by public id"""
        dish = get_dish_summary_by_public_id(int(dish_public_id))
        if not dish:
            api.abort(404)
        else:
            return dish


@api.route('/dish_id=<dish_id>')
@api.param('dish_id', 'dish id')
@api.response(404, 'Dish not found.')
class Dish(Resource):
    @api.doc('get a dish by dish id')
    @api.marshal_with(_dish_detail)
    def get(self, dish_id):
        """get a dish detail by dish id"""
        dish = get_dish_detail_by_id(dish_id)
        if not dish:
            api.abort(404)
        else:
            return dish