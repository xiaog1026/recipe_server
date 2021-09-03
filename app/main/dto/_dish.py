from flask_restx import Namespace, fields

class DishDto:

    api = Namespace('dish', description='dish related operations')

    dish = api.model('dish', {
        'id':fields.Integer(required=True, description='dish id'),
        'public_id': fields.Integer(required=True, description='original dish id'),
        'dishname': fields.String(required=True, description='dish name'),
        'view': fields.Integer(required=True, description='view number'),
        'favorite': fields.Integer(required=True, description='favorite number'),
        'dish_image_link': fields.String(required=True, description='original dish image link'),
        'dish_vedio_link': fields.String(required=True, description='original dish vedio link'),
        'dish_link': fields.String(required=True, description='original dish detail page link'),
        'author_comment': fields.String(required=True, description='the author comment'),
        'tip': fields.String(required=True, description='the author tip'),
        'more_other_recipe_href': fields.String(required=True, description='more other recipe href'),
        'more_replica_href': fields.String(required=True, description='more replica href'),
        'more_relative_recommendaton_href': fields.String(required=True, description='more relative recommendation href'),
        'user_public_id': fields.String(required=True, description='user public id')
    })

    new_dish = api.model('new_dish', {
        'public_id': fields.Integer(required=True, description='original dish id'),
        'dishname': fields.String(required=True, description='dish name'),
        'view': fields.Integer(required=True, description='view number'),
        'favorite': fields.Integer(required=True, description='favorite number'),
        'dish_image_link': fields.String(required=True, description='original dish image link'),
        'dish_vedio_link': fields.String(required=True, description='original dish vedio link'),
        'dish_link': fields.String(required=True, description='original dish detail page link'),
        'author_comment': fields.String(required=True, description='the author comment'),
        'tip': fields.String(required=True, description='the author tip'),
        'more_other_recipe_href': fields.String(required=True, description='more other recipe href'),
        'more_replica_href': fields.String(required=True, description='more replica href'),
        'more_relative_recommendaton_href': fields.String(required=True, description='more relative recommendation href'),
        'tags': fields.List(cls_or_instance=fields.String, required=True, description='tags',),
        'user_public_id': fields.String(required=True, description='user public id')
    })


    nutrition_field = {}
    nutrition_field['nutrition_rate'] = fields.Float(required=True, description='nutrition rate')
    nutrition_field['nutrition_name'] = fields.String(required=True, description='nutrition name')
    nutrition_field['nutrition_weight'] = fields.Float(required=True, description='nutrition weight')

    ingredient_field = {}
    ingredient_field['ingredent_name'] = fields.String(required=True, description='ingredent name')
    ingredient_field['ingredent_weight'] = fields.Float(required=True, description='ingredent weight')
    ingredient_field['ingredent_unit'] = fields.String(required=True, description='ingredent unit')

    step_field = {}
    step_field['step_description'] = fields.String(required=True, description='step description')
    step_field['step_image'] = fields.String(required=True, description='step image')

    rating_field = {}
    rating_field['max'] = fields.Float(required=True, description='rating max')
    rating_field['average'] = fields.Float(required=True, description='rating average')
    rating_field['stars'] = fields.Float(required=True, description='rating stars')
    rating_field['min'] = fields.Float(required=True, description='rating min')

    imitation_field = {}
    imitation_field['user'] = fields.String(required=True, description='user cook the recipe')
    imitation_field['comment_content'] = fields.String(required=True, description='comment content')
    imitation_field['comment_date'] = fields.DateTime(required=True, description='comment date')
    imitation_field['image'] = fields.String(required=True, description='image link')

    dish_detail = api.model('dish_detail', {
        'id': fields.Integer(required=True, description='dish id'),
        'dishname': fields.String(required=True, description='dish name'),
        'author': fields.String(required=True, description='user name'),
        "level": fields.String(required=True, description='level'),# null
        "tool": fields.String(required=True, description='level'),# null
        'dish_image_link': fields.String(required=True, description='original dish image link'),
        'dish_vedio_link': fields.String(required=True, description='original dish vedio link'),
        'nutritions': fields.List(cls_or_instance=fields.Nested(api.model('nutrition', nutrition_field)), required=True, description='nutritions'),
        'ingredients': fields.List(cls_or_instance=fields.Nested(api.model('ingredient', ingredient_field)), required=True, description='ingredients'),
        'steps': fields.List(cls_or_instance=fields.Nested(api.model('step', step_field)), required=True, description='steps'),
        'rating':fields.Nested(api.model('rating', rating_field), required=True, description='rating'),
        'comments': fields.List(cls_or_instance=fields.Nested(api.model('imitation', imitation_field)), required=True, description='steps'),
    })