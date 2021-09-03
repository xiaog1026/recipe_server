import random
from flask import request
from flask_restx import Resource
from ..dto._recommendation_condition import RecommendationConditionDto
from ..service import recommendation_condition as re_co_service

api = RecommendationConditionDto.api
_new_recommendation_conditions = RecommendationConditionDto.new_recommendation_conditions
_current_recommendation_conditions = RecommendationConditionDto.current_recommendation_conditions

@api.route('/user_id=<user_id>')
class RecommendationConditionList(Resource):

    @api.doc('recommendation condition list')
    @api.marshal_list_with(_current_recommendation_conditions, envelope='data')
    def get(self, user_id):
        """List up recommendation conditions"""
        return re_co_service.get_recommendation_conditions(user_id)

    @api.response(201, 'recommendation condition successfully updated.')
    @api.doc('update recommendation condition')
    @api.expect(_new_recommendation_conditions, validate=True)
    def post(self, user_id):
        """update recommendation conditions for the user delete all old ones , and save all new ones """
        data = request.json
        return re_co_service.update_recommendation_conditions(data)