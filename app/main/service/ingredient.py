import uuid
import datetime

from app.main import db
from app.main.model.ingredient import Ingredient


def save_new_ingredient(data):
    ingredient = Ingredient.query.filter_by(dish_id=data['dish_id'], ingredientname=data['ingredientname']).first()
    if not ingredient:
        new_ingredient = Ingredient(
            ingredientname = data['ingredientname'],
            weight = data['weight'],
            dish_id=data['dish_id'],
        )

        save_changes(new_ingredient)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Ingredient already exists.',
        }
        return response_object, 409


def get_all_ingredients():
    return Ingredient.query.all()

def get_all_ingredients_of_dish(dish_id):
    return Ingredient.query.filter_by(dish_id=dish_id).all()

def get_a_ingredient(id):
    return Ingredient.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()