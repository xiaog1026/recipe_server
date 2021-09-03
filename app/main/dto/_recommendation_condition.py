from flask_restx import Namespace, fields

class RecommendationConditionDto:

    api = Namespace('recommendation_condition', description='recommendation_condition related operations')

    new_recommendation_condition_field = {
        'condition_name': fields.String(required=True, description='condition name'),
        'condition_code': fields.Integer(required=True, description='condition code'),
        'condition_scope_name': fields.String(required=True, description='condition scope name'),
        'condition_scope_code': fields.Integer(required=True, description='condition scope code'),
        'condition_value': fields.Float(required=True, description='condition value'),
    }

    current_recommendation_condition_field = {
        'user_id': fields.Integer(required=True, description='user id'),
        'condition_name': fields.String(required=True, description='condition name'),
        'condition_code': fields.Integer(required=True, description='condition code'),
        'condition_scope_name': fields.String(required=True, description='condition scope name'),
        'condition_scope_code': fields.Integer(required=True, description='condition scope code'),
        'condition_value': fields.Float(required=True, description='condition value'),
        'updated_at': fields.Float(required=True, description='updated datetime'),
    }

    new_recommendation_conditions = api.model('new_recommendation_conditions', {
        'user_id': fields.Integer(required=True, description='user id'),
        'recommendation_conditions': fields.List(cls_or_instance=fields.Nested(api.model('new_recommendation_condition', new_recommendation_condition_field)), required=True,
                                                 description='new_recommendation_condition'),
    })

    current_recommendation_conditions = api.model('current_recommendation_conditions', {
        'user_id': fields.Integer(required=True, description='user id'),
        'recommendation_conditions': fields.List(
            cls_or_instance=fields.Nested(api.model('current_recommendation_condition', current_recommendation_condition_field)),
            required=True,
            description='current_recommendation_condition'),
    })