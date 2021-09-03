from flask_restx import Namespace, fields

class IngredientDto:
    api = Namespace('ingredient', description='ingredient related operations')
    ingredient = api.model('ingredient', {
        'id': fields.Integer(required=True, description='ingredient id'),
        'ingredientname': fields.String(required=True, description='ingredient name'),
        'weight': fields.String(required=True, description='ingredient weight'),
        'dish_id': fields.Integer(required=True, description='what dish id these ingredients are used for'),
    })
    new_ingredient = api.model('new_ingredient', {
        'ingredientname': fields.String(required=True, description='ingredient name'),
        'weight': fields.String(required=True, description='ingredient weight'),
        'dish_id': fields.Integer(required=True, description='what dish id these ingredients are used for'),
    })