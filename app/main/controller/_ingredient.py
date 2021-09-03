from flask import request
from flask_restx import Resource

from ..dto._ingredient import IngredientDto
from ..service.ingredient import save_new_ingredient, get_all_ingredients, get_a_ingredient, get_all_ingredients_of_dish

api = IngredientDto.api
_ingredient = IngredientDto.ingredient
_new_ingredient = IngredientDto.new_ingredient


@api.route('/')
class IngredientList(Resource):
    @api.doc('list up all ingredients')
    @api.marshal_list_with(_ingredient, envelope='data')
    def get(self):
        """List all registered ingredients"""
        return get_all_ingredients()

    @api.response(201, 'Ingredient successfully created.')
    @api.doc('create a new ingredient')
    @api.expect(_new_ingredient, validate=True)
    def post(self):
        """Creates a new ingredient """
        data = request.json
        return save_new_ingredient(data=data)


@api.route('/dish_id=<dish_id>')
@api.param('dish_id', 'dish id')
@api.response(404, 'Ingredient not found.')
class IngredientListInDish(Resource):
    @api.doc('get all ingredients used in the dish')
    @api.marshal_list_with(_ingredient)
    def get(self, dish_id):
        """get all registered ingredients of a dish"""
        return get_all_ingredients_of_dish(dish_id)


@api.route('/id=<id>')
@api.param('id', 'ingredient id')
@api.response(404, 'Ingredient not found.')
class Ingredient(Resource):
    @api.doc('get a ingredient')
    @api.marshal_with(_ingredient)
    def get(self, id):
        """get a ingredient given its identifier"""
        ingredient = get_a_ingredient(id)
        if not ingredient:
            api.abort(404)
        else:
            return ingredient