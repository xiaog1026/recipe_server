from flask_restx import Namespace, fields

class StepDto:
    api = Namespace('step', description='step related operations')
    step = api.model('step', {
        'id': fields.Integer(required=True, description='step id'),
        'step_no': fields.Integer(required=True, description='cook step no'),
        'step_description': fields.String(required=True, description='cook step description'),
        'step_image_link': fields.String(required=True, description='cook step link'),
        'dish_id': fields.Integer(required=True, description='what dish id are the cook step for'),
    })
    new_step = api.model('new_step', {
        'step_no': fields.Integer(required=True, description='cook step no'),
        'step_description': fields.String(required=True, description='cook step description'),
        'step_image_link': fields.String(required=True, description='cook step link'),
        'dish_id': fields.Integer(required=True, description='what dish id are the cook step for'),
    })