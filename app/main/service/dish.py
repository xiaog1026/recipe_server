import uuid
import datetime
import random
from app.main import db
from app.main.model.dish import Dish, dish_m2m_tag
from app.main.model.tag import Tag
from app.main.model.user import User
from app.main.model.replica import Replica
from app.main.model.comment import Comment
from app.main.model.ingredient import Ingredient
from app.main.model.step import Step
from app.main.service import tag as tag_service
from app.main.service import user as user_service
from app.main.service import comment as comment_service
from app.main.service import replica as replica_service
import logging
import re
from sqlalchemy import desc, asc

logger = logging.getLogger('dish service')

def save_new_dish(data):
    dish = Dish.query.filter_by(public_id=data['public_id']).first()
    if not dish:
        new_dish = Dish(
            public_id = data['public_id'],
            dishname = data['dishname'],
            view=data['view'],
            favorite=data['favorite'],
            dish_image_link=data['dish_image_link'],
            dish_vedio_link=data['dish_vedio_link'],
            dish_link=data['dish_link'],
            author_comment=data['author_comment'],
            tip=data['tip'],
            more_other_recipe_href=data['more_other_recipe_href'],
            more_replica_href=data['more_replica_href'],
            more_relative_recommendaton_href=data['more_relative_recommendaton_href'],
        )
        for tagname_ in data['tags']:
            tag_ = tag_service.get_a_tag_by_name(tagname_)
            if tag_:
                new_dish.tags.append(tag_)
            else:
                response_object = {
                    'status': 'fail',
                    'message': f'tag {tagname_} does not exist'
                }
                return response_object, 409
                # new_tag = Tag(tagname=tagname_)
                # tag_service.save_changes(new_tag)
                # new_dish.tags.append(new_tag)
        user_ = user_service.get_a_user(data['user_public_id'])
        if user_:
            new_dish.user_id = user_.id
        else:
            response_object = {
                'status': 'fail',
                'message': f'user does not exist'
            }
            return response_object, 409

        db.session.add(new_dish)
        db.session.commit()

        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Dish already exists.',
        }
        return response_object, 409


def get_dish_summary():
    return Dish.query.all()

def get_dish_summary_by_tag(tag_id):
    return db.session.query(Dish).join(dish_m2m_tag).filter(dish_m2m_tag.c.tag_id == tag_id).all()

def get_dish_summary_by_id(dish_id):
    return Dish.query.filter_by(id=dish_id).first()

def get_dish_summary_by_public_id(dish_public_id):
    return Dish.query.filter_by(public_id=dish_public_id).first()

def get_dish_detail_by_id(dish_id):

    dish = db.session.query(Dish, User).join(User).filter(Dish.id == dish_id).first()
    ingredients = Ingredient.query.filter_by(dish_id=dish_id).all()
    steps = Step.query.filter_by(dish_id=dish_id).order_by(asc(Step.step_no)) .all()
    replicas = db.session.query(Replica, User).join(User).filter(Replica.dish_id == dish_id).all()
    dish_dict_ = {}
    if dish:
        dish_dict_ = dish[0].__dict__
        dish_dict_['author'] = dish[1].username
        dish_dict_['level'] = ""
        dish_dict_['tool'] = ""
        dish_dict_['ingredients'] = []
        for ingredient_ in ingredients:
            weight_ = re.search('[0-9]+', ingredient_.weight)
            if weight_ is None:
                weight_ = 2
                unit_ = 'g'
            else:
                unit_ = ingredient_.weight.replace(weight_[0], '')
                weight_ = float(weight_[0])
            dish_dict_['ingredients'].append({"ingredent_name":ingredient_.ingredientname, "ingredent_weight":weight_, "ingredent_unit":unit_,})
        dish_dict_['steps'] = []
        for step_ in steps:
            dish_dict_['steps'].append({"step_description": step_.step_description, "step_image": step_.step_image_link, })
        dish_dict_['comments'] = []
        for replica_ in replicas:
            dish_dict_['comments'].append({'user':replica_[1].username, "comment_content":replica_[0].comment, 'image':replica_[0].replica_image_href, 'comment_date':None})

        dish_dict_['rating'] = {
            'min':0,
            'max':10,
            'average':9.3,
            'stars':10,
        }
        dish_dict_['nutritions'] = [
            {
                "nutrition_rate": random.random()*2621.5,
                "nutrition_name": "能量(千卡)",
                "nutrition_weight": 2621.5
            },
            {
                "nutrition_rate": random.random() * 10.98,
                "nutrition_name": "盐(克)",
                "nutrition_weight": 10.98
            },
            {
                "nutrition_rate": random.random() * 76.06,
                "nutrition_name": "蛋白质(克)",
                "nutrition_weight": 76.06
            },
            {
                "nutrition_rate": random.random() * 74.86,
                "nutrition_name": "脂质(克)",
                "nutrition_weight": 74.86
            },
            {
                "nutrition_rate": random.random() * 393.225,
                "nutrition_name": "碳水化合物(克)",
                "nutrition_weight": 393.225
            },
            {
                "nutrition_rate": random.random() * 24.32,
                "nutrition_name": "膳食纤维(克)",
                "nutrition_weight": 24.32
            },
            {
                "nutrition_rate": random.random() * 3000.0,
                "nutrition_name": "钾(毫克)",
                "nutrition_weight": 3000.01
            },
            {
                "nutrition_rate": random.random() * 750.0,
                "nutrition_name": "钙(毫克)",
                "nutrition_weight": 750.01
            },
            {
                "nutrition_rate": random.random() * 7.5,
                "nutrition_name": "铁(毫克)",
                "nutrition_weight": 7.5
            },
            {
                "nutrition_rate": random.random() * 11.0,
                "nutrition_name": "锌(毫克)",
                "nutrition_weight": 11.01
            },
            {
                "nutrition_rate": random.random() * 370.0,
                "nutrition_name": "镁(毫克)",
                "nutrition_weight": float(370.01)
            },
            {
                "nutrition_rate": random.random() * 240.0,
                "nutrition_name": "叶酸(微克)",
                "nutrition_weight": 240.01
            },
            {
                "nutrition_rate": random.random() * 100.0,
                "nutrition_name": "维生素C(毫克)",
                "nutrition_weight": 100.01
            },
            {
                "nutrition_rate": random.random() * 1.3,
                "nutrition_name": "维生素B1(毫克)",
                "nutrition_weight": 1.3
            },
            {
                "nutrition_rate": random.random() * 1.5,
                "nutrition_name": "维生素B2(毫克)",
                "nutrition_weight": 1.5
            },
            {
                "nutrition_rate": random.random() * 50.0,
                "nutrition_name": "维生素D(毫克)",
                "nutrition_weight": 50.01
            },
            {
                "nutrition_rate": random.random() * 2.4,
                "nutrition_name": "维生素B12(毫克)",
                "nutrition_weight": 2.4
            },
            {
                "nutrition_rate": random.random() * 1.4,
                "nutrition_name": "维生素B6(毫克)",
                "nutrition_weight": 1.4
            },
        ]


    return dish_dict_

def save_changes(data):
    db.session.add(data)
    db.session.commit()