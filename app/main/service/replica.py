import uuid
import datetime

from app.main import db
from app.main.model.replica import Replica

def save_new_replica(data):
    replica = Replica.query.filter_by(dish_id=data['dish_id'], user_id=data['user_id']).first()
    if not replica:
        new_replica = Replica(
            replica_href=data['replica_href'],
            replica_image_href=data['replica_image_href'],
            comment=data['comment'],
            dish_id = data['dish_id'],
            user_id = data['user_id'],
        )
        save_changes(new_replica)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Replica already exists.',
        }
        return response_object, 409


def get_all_replicas():
    return Replica.query.all()

def get_all_replicas_of_dish(dish_id):
    return Replica.query.filter_by(dish_id=dish_id).all()

def get_a_replica(id):
    return Replica.query.filter_by(id=id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()