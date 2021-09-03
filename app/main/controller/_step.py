from flask import request
from flask_restx import Resource

from ..dto._step import StepDto
from ..service.step import save_new_step, get_all_steps, get_a_step, get_all_steps_of_dish

api = StepDto.api
_step = StepDto.step
_new_step = StepDto.new_step


@api.route('/')
class StepList(Resource):
    @api.doc('list_of_registered_steps')
    @api.marshal_list_with(_step, envelope='data')
    def get(self):
        """List all registered steps"""
        return get_all_steps()

    @api.response(201, 'Step successfully created.')
    @api.doc('create a new step')
    @api.expect(_new_step, validate=True)
    def post(self):
        """Creates a new Step """
        data = request.json
        return save_new_step(data=data)


@api.route('/<dish_id>')
@api.param('dish_id', 'dish id')
@api.response(404, 'Steps not found.')
class Step(Resource):
    @api.doc('get all steps of a dish')
    @api.marshal_list_with(_step)
    def get(self, dish_id):
        """get all step of a dish given its identifier"""
        return get_all_steps_of_dish(dish_id)

@api.route('/id=<id>')
@api.param('id', 'step id')
@api.response(404, 'Step not found.')
class Ingredient(Resource):
    @api.doc('get a step of a dish')
    @api.marshal_with(_step)
    def get(self, id):
        """get a step given its identifier"""
        step = get_a_step(id)
        if not step:
            api.abort(404)
        else:
            return step
