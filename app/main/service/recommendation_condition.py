import uuid
import datetime
import pandas as pd
from app.main import db
from app.main.model.recommendation_condition import RecommendationCondition



class RECOMMENDATION_CONDITION_CODE:
    N_PERSON_WITH_BAD_TEETH = 2
    N_KIDS = 3
    N_DISHS = 4
    N_PERSON = 5
    COOKING_TIME = 6
    COST = 7

class RECOMMENDATION_CONDITION_SCOPE_CODE:
    VALID_INGREDENTS = 1
    N_PERSON_WITH_BAD_TEETH = 2
    N_KIDS = 3
    N_DISHS = 4
    N_PERSON = 5
    COOKING_TIME = 6
    COST = 7
    FAVORITE_INGREDIENTS = 8
    UNLIKE_INGREDIENTS = 9
    FAVORITE_FLAVOR = 10
    COOKING_METHOD = 11
    MEDICAL_HISTORY = 12

class RECOMMENDATION_CONDITION_SCOPE_VAL:
    VALID_INGREDENTS = 'valid_ingredents'
    N_PERSON_WITH_BAD_TEETH = 'n_person_with_bad_teeth'
    N_KIDS = 'n_kids'
    N_DISHS = 'n_dishs'
    N_PERSON = 'n_person'
    COOKING_TIME = 'cooking_time'
    COST = 'cost'
    FAVORITE_INGREDIENTS = 'favorite_ingredients'
    UNLIKE_INGREDIENTS = 'unlike_ingredients'
    FAVORITE_FLAVOR = 'favorite_flavor'
    COOKING_METHOD = 'cooking_method'
    MEDICAL_HISTORY = 'medical_history'
    LIST = [VALID_INGREDENTS, N_PERSON_WITH_BAD_TEETH, N_KIDS, N_DISHS, N_PERSON, COOKING_TIME, COST, FAVORITE_INGREDIENTS,
            UNLIKE_INGREDIENTS, FAVORITE_FLAVOR, COOKING_METHOD, MEDICAL_HISTORY, ]

def update_recommendation_conditions(data):

    user_id = data['user_id']
    old_conditions = RecommendationCondition.query.filter_by(user_id=user_id).all()
    try:
        for condition_i in old_conditions:
            db.session.delete(condition_i)

        for condition_i in data['recommendation_conditions']:
            new_condition_i = RecommendationCondition(
                condition_name=condition_i['condition_name'],
                condition_code=condition_i['condition_code'],
                condition_scope_name=condition_i['condition_scope_name'],
                condition_scope_code=condition_i['condition_scope_code'],
                condition_value=condition_i['condition_value'],
                user_id=user_id,
            )
            db.session.add(new_condition_i)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully updated.'
        }
        http_code = 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'updating failed.',
        }
        http_code = 409

    return response_object, http_code


def get_recommendation_conditions(user_id):
    return RecommendationCondition.query.filter_by(user_id=user_id).all()

def set_default_recommendation_conditions(user_id):

    recommendation_conditions = []

    rc_ = RecommendationCondition(
        condition_name='猪肉',
        condition_code=234,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.VALID_INGREDENTS,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.VALID_INGREDENTS,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='大白菜',
        condition_code=55,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.VALID_INGREDENTS,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.VALID_INGREDENTS,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='需要菜数',
        condition_code=RECOMMENDATION_CONDITION_CODE.N_DISHS,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.N_DISHS,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.N_DISHS,
        condition_value=5,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='牙口不好的人',
        condition_code=RECOMMENDATION_CONDITION_CODE.N_PERSON_WITH_BAD_TEETH,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.N_PERSON_WITH_BAD_TEETH,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.N_PERSON_WITH_BAD_TEETH,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='小孩',
        condition_code=RECOMMENDATION_CONDITION_CODE.N_KIDS,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.N_KIDS,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.N_KIDS,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='人数',
        condition_code=RECOMMENDATION_CONDITION_CODE.N_PERSON,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.N_PERSON,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.N_PERSON,
        condition_value=5,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='做饭时间',
        condition_code=RECOMMENDATION_CONDITION_CODE.COOKING_TIME,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.COOKING_TIME,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.COOKING_TIME,
        condition_value=30,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='费用',
        condition_code=RECOMMENDATION_CONDITION_CODE.COST,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.COST,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.COST,
        condition_value=50,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='猪肉',
        condition_code=100,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.FAVORITE_INGREDIENTS,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.FAVORITE_INGREDIENTS,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='鸭肉',
        condition_code=200,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.UNLIKE_INGREDIENTS,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.UNLIKE_INGREDIENTS,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='咸',
        condition_code=300,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.FAVORITE_FLAVOR,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.FAVORITE_FLAVOR,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='砂锅',
        condition_code=400,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.COOKING_METHOD,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.COOKING_METHOD,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    rc_ = RecommendationCondition(
        condition_name='糖尿病',
        condition_code=400,
        condition_scope_name=RECOMMENDATION_CONDITION_SCOPE_VAL.MEDICAL_HISTORY,
        condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.MEDICAL_HISTORY,
        condition_value=1,
        user_id=user_id,
    )
    recommendation_conditions.append(rc_)

    for condition_i in recommendation_conditions:
        new_condition_i = RecommendationCondition(
            condition_name=condition_i.condition_name,
            condition_code=condition_i.condition_code,
            condition_scope_name=condition_i.condition_scope_name,
            condition_scope_code=condition_i.condition_scope_code,
            condition_value=condition_i.condition_value,
            user_id=user_id,
        )
        db.session.add(new_condition_i)
    db.session.commit()
    return

def update_ingredient_recommendation_condition(user_id, data):
    old_conditions = RecommendationCondition.query.filter_by(user_id=user_id, condition_scope_code=RECOMMENDATION_CONDITION_SCOPE_CODE.VALID_INGREDENTS).all()
    for c in old_conditions:
        db.session.delete(c)

    for condition_i in data['recommendation_conditions']:
        new_condition_i = RecommendationCondition(
            condition_name=condition_i['condition_name'],
            condition_code=condition_i['condition_code'],
            condition_scope_name=condition_i['condition_scope_name'],
            condition_scope_code=condition_i['condition_scope_code'],
            condition_value=condition_i['condition_value'],
            user_id=user_id,
        )
        db.session.add(new_condition_i)
    db.session.commit()
    return

def update_genernal_recommendation_condition(user_id, data):
    old_conditions = db.session.query(RecommendationCondition).filter(RecommendationCondition.user_id == user_id,
                                                                      RecommendationCondition.condition_scope_code!=RECOMMENDATION_CONDITION_SCOPE_CODE.VALID_INGREDENTS).all()
    for c in old_conditions:
        db.session.delete(c)

    for condition_i in data['recommendation_conditions']:
        new_condition_i = RecommendationCondition(
            condition_name=condition_i['condition_name'],
            condition_code=condition_i['condition_code'],
            condition_scope_name=condition_i['condition_scope_name'],
            condition_scope_code=condition_i['condition_scope_code'],
            condition_value=condition_i['condition_value'],
            user_id=user_id,
        )
        db.session.add(new_condition_i)
    db.session.commit()
    return


def format_recommendation_condition(recommendation_conditions):

    recommendation_condition_df = pd.DataFrame([r.__dict__ for r in recommendation_conditions])
    formated_output = {}
    for item in RECOMMENDATION_CONDITION_SCOPE_VAL.LIST:
        formated_output[item] = list(recommendation_condition_df[recommendation_condition_df['condition_scope_name']==item].T.to_dict().values())
    return formated_output

def save_changes(data):
    db.session.add(data)
    db.session.commit()
