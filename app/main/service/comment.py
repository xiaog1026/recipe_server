import uuid
# import datetime
from datetime import datetime

from app.main import db
from app.main.model.comment import Comment


def save_new_comment(data):
    comment = Comment.query.filter_by(dish_id=data['dish_id'], user_id=data['user_id']).first()
    if not comment:
        new_comment = Comment(
            comment = data['comment'],
            comment_date = datetime.strptime(data['comment_date'], "%Y-%m-%dT%H:%M:%S.%fZ"),
            user_herf=data['user_herf'],
            dish_id=data['dish_id'],
            user_id=data['user_id'],
        )

        save_changes(new_comment)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Comment already exists.',
        }
        return response_object, 409


def get_all_comments():
    return Comment.query.all()

def get_all_comments_of_dish(dish_id):
    return Comment.query.filter_by(dish_id=dish_id).all()

def get_a_comment(dish_id, user_id):
    return Comment.query.filter_by(dish_id=dish_id, user_id=user_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()