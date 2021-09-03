from flask_restx import Namespace, fields

class CardDto:
    api = Namespace('card', description='card related operations')

    dish_field = {}
    dish_field['dish_id'] = fields.Integer(required=True, description='dish id')
    dish_field['dish_name'] = fields.String(required=True, description='dish name')
    dish_field['dish_image_link'] = fields.String(required=True, description='dish image link date')

    card_field = {}
    card_field['dish_type'] = fields.String(required=True, description='dish type, also a card type name')
    card_field['dish_type_name'] = fields.String(required=True, description='dish type name, also a tag name')
    card_field['dish_count'] = fields.Integer(required=True, description='dish count')
    card_field['dish'] = fields.List(cls_or_instance=fields.Nested(api.model('dish', dish_field)), required=True, description='dish list')

    ingreditent_field = {}
    ingreditent_field['ingredent_name'] = fields.String(required=True, description='ingredient name')
    ingreditent_field['ingredent_weight'] = fields.Integer(required=True, description='ingredient weight')
    ingreditent_field['ingredent_unit'] = fields.String(required=True, description='ingredient weight unit')

    recommend_base_condition_field = {}
    recommend_base_condition_field['side_dish_base_name'] = fields.String(required=True, description='recommend base condition describe')
    recommend_base_condition_field['side_dish_base_num'] = fields.Integer(required=True, description='recommend base condition')
    recommend_base_condition_field['side_dish_base_unit'] = fields.String(required=True, description='recommend base condition unit')

    recommend_personal_condition_likes_field = {}
    recommend_personal_condition_likes_field['side_dish_option_like_name'] = fields.String(required=True, description='recommend personal condition name')
    recommend_personal_condition_likes_field['side_dish_option_like_status'] = fields.Integer(required=True, description='recommend personal condition status')

    recommend_personal_condition_hates_field = {}
    recommend_personal_condition_hates_field['side_dish_option_hate_name'] = fields.String(required=True, description='recommend personal condition name')
    recommend_personal_condition_hates_field['side_dish_option_hate_status'] = fields.Integer(required=True, description='recommend personal condition status')

    recommend_personal_condition_hates_field = {}
    recommend_personal_condition_hates_field['side_dish_option_hate_name'] = fields.String(required=True, description='recommend personal condition name')
    recommend_personal_condition_hates_field['side_dish_option_hate_status'] = fields.Integer(required=True, description='recommend personal condition status')

    recommend_flavor_condition_field = {}
    recommend_flavor_condition_field['side_dish_option_taste_name'] = fields.String(required=True, description='recommend flavor condition name')
    recommend_flavor_condition_field['side_dish_option_taste_status'] = fields.Integer(required=True, description='recommend flavor condition status')

    cards = api.model('cards', {
        'cards':fields.List(cls_or_instance=fields.Nested(api.model('card', card_field)), required=True, description='comments')
    })