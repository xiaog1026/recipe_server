from flask_restx import Resource
from flask import request
from werkzeug.datastructures import FileStorage
from app.main.dto.table import TableDto
from app.main.service import recommendation_condition as re_co_service
from app.main.service import recommendation as re_service
from app.main.business import table as table_service
import numpy as np
import io
import cv2
# from flask_restx import Api, Resource

api = TableDto.api
_current_table = TableDto.table
_other_candidate_cards = TableDto.other_candidate_cards
_ingredient_recommendation_condition = TableDto.ingredient_recommendation_condition
_genernal_recommendation_condition = TableDto.genernal_recommendation_condition
_detected_ingredient = TableDto.detected_ingredient

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)



@api.route('/user_id=<user_id>')
@api.param('user_id', 'user id')
@api.response(404, 'table not found.')
class TableInit(Resource):
    @api.doc('get table of a user by default condition. use this request for init table page')
    @api.marshal_with(_current_table)
    def get(self, user_id):
        """recommend a meal for the user, if can not find recommendation then what should we do? """

        table_init = None
        try:
            user_id = int(user_id)
        except Exception as e:
            api.abort(400, custom=f'invalid input {e.__str__()}')

        try:
            today_recommendations = re_service.get_today_recommendation(user_id)
            formated_today_recommendations = []
            if len(today_recommendations) == 0:
                table_service.recommend(user_id)
                today_recommendations = re_service.get_today_recommendation(user_id)
            recommendation_conditions = re_co_service.get_recommendation_conditions(user_id)
            for r in today_recommendations:
                d_ = {}
                d_['dish_id'] = r[1].id
                d_['dish_name'] = r[1].dishname
                d_['dish_image_link'] = r[1].dish_image_link
                d_['tag_id'] = r[2].id
                d_['tag_name'] = r[2].tagname

                formated_today_recommendations.append(d_)

            table_init = {
                'user_id': user_id,
                'current_recommendation': {
                    'dish_count':len(formated_today_recommendations),
                    'dish': formated_today_recommendations,
                },
                'current_recommend_condition_summary': re_co_service.format_recommendation_condition(recommendation_conditions),
            }

        except Exception as e:
            api.abort(400, custom=f'extract card info error {e.__str__()}')

        return table_init

@api.route('/other_candidate/user_id=<user_id>')
@api.param('user_id', 'user id')
@api.response(404, 'other_candidate not found.')
class OtherCandidate(Resource):
    @api.doc('find other candidate for the user')
    @api.marshal_with(_other_candidate_cards)
    def get(self, user_id):
        """get other candidate of today recommendation"""
        try:
            user_id = int(user_id)
        except Exception as e:
            api.abort(400, custom=f'invalid input {e.__str__()}')

        today_recommendations = re_service.get_today_recommendation(user_id)
        if len(today_recommendations) == 0:
            table_service.recommend(user_id)
            today_recommendations = re_service.get_today_recommendation(user_id)

        cards = None
        try:
            cards = table_service.other_candidate(today_recommendations)
        except Exception as e:
            api.abort(400, custom=f'extract card info error {e.__str__()}')

        return cards

@api.route('/ingredient_recommendation_condition/user_id=<user_id>')
@api.param('user_id', 'user id')
@api.response(404, 'update ingredient recommendation condition not found.')
class UpdateIngredientCondition(Resource):
    @api.doc('update ingredient recommendation condition')
    @api.expect(_ingredient_recommendation_condition, validate=True)
    def post(self, user_id):
        """update the ingredient recommendation conditions """
        data = request.json
        re_co_service.update_ingredient_recommendation_condition(int(user_id), data)
        response_object = {
            'status': 'success',
            'message': 'updated successfully.'
        }
        return response_object, 201

@api.route('/genernal_recommendation_condition/user_id=<user_id>')
@api.param('user_id', 'user id')
@api.response(404, 'update genernal recommendation condition not found.')
class UpdateGenernalCondition(Resource):
    @api.doc('update genernal recommendation condition')
    @api.expect(_genernal_recommendation_condition, validate=True)
    def post(self, user_id):
        """update the genernal recommendation conditions """
        data = request.json
        re_co_service.update_genernal_recommendation_condition(int(user_id), data)
        response_object = {
            'status': 'success',
            'message': 'updated successfully.'
        }
        return response_object, 201

@api.route('/ingredient_recognition')
@api.expect(upload_parser)
@api.response(404, 'recognize the ingredient in the image')
class Recommendation(Resource):
    @api.doc('recognize the ingredient in the image')
    @api.marshal_with(_detected_ingredient)
    def post(self):
        """upload a image , recognize the ingredient """
        args = upload_parser.parse_args()
        image = args.get('file')
        in_memory_file = io.BytesIO()
        image.save(in_memory_file)
        data = np.fromstring(in_memory_file.getvalue(), dtype=np.uint8)
        color_image_flag = 1
        img = cv2.imdecode(data, color_image_flag)
        height_ = img.shape[0]
        width_ = img.shape[1]
        dummy_detection = {
            'annotations':[
                {
                    'x1': 1,
                    'y1': 1,
                    'x2': width_ * .5,
                    'y2': height_ * .5,
                    'label': '香菜',
                },
            ]
        }
        return dummy_detection