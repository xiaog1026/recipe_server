import uuid
import datetime

from app.main import db
from app.main.model.tag import Tag


def save_new_tag(data):
    tag = Tag.query.filter_by(tagname=data['tagname']).first()
    if not tag:
        new_tag = Tag(
            tagname=data['tagname'],
        )
        save_changes(new_tag)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Tag already exists.',
        }
        return response_object, 409


def get_tags():
    return Tag.query.all()

def get_tags_page():
    return Tag.query.all()

def get_tag_page(page, per_page):
    return Tag.query.order_by(Tag.id).paginate(page, per_page, error_out=False)

def get_a_tag_by_name(tagname):
    return Tag.query.filter_by(tagname=tagname).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()