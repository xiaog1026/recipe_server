import uuid
import datetime

from app.main import db
from app.main.model.step import Step


def save_new_step(data):
    step = Step.query.filter_by(dish_id=data['dish_id'], step_no=data['step_no']).first()
    if not step:
        new_step = Step(
            step_no=data['step_no'],
            step_description=data['step_description'],
            step_image_link=data['step_image_link'],
            dish_id = data['dish_id']
        )
        save_changes(new_step)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Step already exists.',
        }
        return response_object, 409


def get_all_steps():
    return Step.query.all()

def get_all_steps_of_dish(dish_id):
    return Step.query.filter_by(dish_id=dish_id).all()

def get_a_step(id):
    return Step.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()