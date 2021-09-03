from flask_restx import Namespace, fields

class TableDto:

    api = Namespace('table', description='table related operations')

    dish_field = {}
    dish_field['dish_id'] = fields.Integer(required=True, description='dish id')
    dish_field['dish_name'] = fields.String(required=True, description='dish name')
    dish_field['dish_image_link'] = fields.String(required=True, description='dish image link date')
    dish_field['tag_id'] = fields.String(required=True, description='main ingredient tag id')
    dish_field['tag_name'] = fields.String(required=True, description='main ingredient tag name')

    recommendation_field = {
        'dish_count': fields.Integer(required=True, description='dish card count'),
        'dish': fields.List(cls_or_instance=fields.Nested(api.model('dish', dish_field)), required=True, description='dish list'),
    }

    condition_field = {
        'condition_name': fields.String(required=True, description='condition name'),
        'condition_code': fields.Integer(required=True, description='condition name'),
        'condition_value': fields.Float(required=True, description='condition value'),
    }

    recommend_condition_summary_field = {
        'valid_ingredents': fields.List(cls_or_instance=fields.Nested(api.model('valid_ingredents', condition_field)),
                                        required=True, description='valid ingredient list'),
        'n_person_with_bad_teeth': fields.List(cls_or_instance=fields.Nested(api.model('n_person_with_bad_teeth', condition_field)),
                                        required=True, description='how many person with bad teeth'),
        'n_kids': fields.List(cls_or_instance=fields.Nested(api.model('n_kids', condition_field)),
                                        required=True, description='how many kids'),
        'n_dishs': fields.List(cls_or_instance=fields.Nested(api.model('n_dishs', condition_field)),
                                        required=True, description='how many n_dishs'),
        'n_person': fields.List(cls_or_instance=fields.Nested(api.model('n_person', condition_field)),
                                        required=True, description='how many person'),
        'cooking_time': fields.List(cls_or_instance=fields.Nested(api.model('cooking_time', condition_field)),
                                        required=True, description='how long does the cooking need'),
        'cost': fields.List(cls_or_instance=fields.Nested(api.model('cost', condition_field)),
                                        required=True, description='how much does the ingredients need'),
        'favorite_ingredients': fields.List(cls_or_instance=fields.Nested(api.model('favorite_ingredients', condition_field)),
                                        required=True, description='favorite ingredients'),
        'unlike_ingredients': fields.List(cls_or_instance=fields.Nested(api.model('unlike_ingredients', condition_field)),
                                        required=True, description='unlike ingredients'),
        'favorite_flavor': fields.List(cls_or_instance=fields.Nested(api.model('favorite_flavor', condition_field)),
                                        required=True, description='favorite flavor'),
        'cooking_method': fields.List(cls_or_instance=fields.Nested(api.model('cooking_method', condition_field)),
                                        required=True, description='cooking method'),
        'medical_history': fields.List(cls_or_instance=fields.Nested(api.model('medical_history', condition_field)),
                                        required=True, description='medical history'),
    }

    table = api.model('table', {
        'user_id': fields.Integer(required=True, description='user id'),
        'current_recommendation': fields.Nested(api.model('recommendation', recommendation_field), required=True,
            description='recommendation in recommendation page'),
        'current_recommend_condition_summary': fields.Nested(
            api.model('recommend_condition_summary', recommend_condition_summary_field), required=True,
            description='recommend condition summary for display in recommendation page'),
    })

    card_field = {}
    card_field['dish_type_id'] = fields.Integer(required=True, description='dish type id, also a card type name')
    card_field['dish_type_name'] = fields.String(required=True, description='dish type name, also a tag name')
    card_field['dish'] = fields.List(cls_or_instance=fields.Nested(api.model('dish', dish_field)), required=True, description='dish list')

    other_candidate_cards = api.model('other_candidate_cards', {
        'cards':fields.List(cls_or_instance=fields.Nested(api.model('card', card_field)), required=True, description='other recommendation candidate card')
    })

    irc_condition_field = {
        'condition_name': fields.String(required=True, description='condition name'),
        'condition_code': fields.Integer(required=True, description='condition code'),
        'condition_scope_name': fields.String(required=True, description='condition scope name'),
        'condition_scope_code': fields.Integer(required=True, description='condition scope code'),
        'condition_value': fields.Float(required=True, description='condition value'),
    }

    ingredient_recommendation_condition = api.model('ingredient_recommendation_condition', {
        'recommendation_conditions': fields.List(cls_or_instance=fields.Nested(api.model('irc_condition_field', irc_condition_field)), required=True,
                             description='ingredient recommendation condition')
    })

    grc_condition_field = {
        'condition_name': fields.String(required=True, description='condition name'),
        'condition_code': fields.Integer(required=True, description='condition code'),
        'condition_scope_name': fields.String(required=True, description='condition scope name'),
        'condition_scope_code': fields.Integer(required=True, description='condition scope code'),
        'condition_value': fields.Float(required=True, description='condition value'),
    }


    genernal_recommendation_condition = api.model('genernal_recommendation_condition', {
        'recommendation_conditions': fields.List(cls_or_instance=fields.Nested(api.model('grc_condition_field', grc_condition_field)), required=True,
                             description='genernal recommendation condition')
    })

    position_field = {
        'x1': fields.Float(required=True, description='left up point x'),
        'y1': fields.Float(required=True, description='left up point y'),
        'x2': fields.Float(required=True, description='right down point x'),
        'y2': fields.Float(required=True, description='right down point y'),
        'label': fields.String(required=True, description='label'),
    }

    detected_ingredient = api.model('detected_ingredient', {
        'annotations':fields.List(cls_or_instance=fields.Nested(api.model('position_field', position_field)), required=True,
                             description='ingredient position and label')
    })