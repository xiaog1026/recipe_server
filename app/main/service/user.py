import uuid
import datetime
import random
import string
from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(public_id=data['public_id']).first()
    if not user:
        new_user = User(
            public_id=data['public_id'],
            username=data['username'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists.',
        }
        return response_object, 409

def registered_user(account, password):
    public_id = str(uuid.uuid1())
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        new_user = User(
            public_id = public_id,
            username = account,
            password = password,
            registered_on=datetime.datetime.now()
        )
        save_changes(new_user)
        return new_user
    else:
        return None

def change_account_password(id, account, password):

    user = User.query.filter_by(id=id).first()
    if user:
        user.username = account
        user.password = password
        save_changes(user)
        return user
    else:
        return None

def registered_visitor():
    account = ''.join(random.choices(list(string.ascii_letters + string.digits + string.punctuation), k=10))
    password = ''.join(random.choices(list(string.ascii_letters + string.digits + string.punctuation), k=10))
    public_id = str(uuid.uuid1())
    user = User.query.filter_by(public_id=public_id).first()
    if not user:
        new_user = User(
            public_id=public_id,
            username=account,
            password=password,
            registered_on=datetime.datetime.now()
        )
        save_changes(new_user)
        return new_user
    else:
        return None

def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()