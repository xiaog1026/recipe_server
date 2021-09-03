import uuid
import datetime
import pandas as pd
from app.main import db
from app.main.model.recommendation import Recommendation
from app.main.model.dish import Dish
from app.main.model.tag import Tag
from ..service import recommendation_condition as re_co_service
from ..service import tag as tag_service
from ..service import dish as dish_service
from ..service import recommendation as re_service
from datetime import datetime, date, timezone
from app.main.util.constant import *
import random
from sqlalchemy.sql import func


def recommend(user_id):

    conditions = re_co_service.get_recommendation_conditions(user_id)
    if len(conditions) == 0:
        re_co_service.set_default_recommendation_conditions(user_id)
        conditions = re_co_service.get_recommendation_conditions(user_id)

    condition_df = pd.DataFrame([c.__dict__ for c in conditions])
    n_dishs = condition_df[condition_df['condition_scope_name'] == 'n_dishs']['condition_value'].values[0]
    tags = tag_service.get_tags()
    for t_ in random.sample(tags, int(n_dishs)):
        dishs_ = dish_service.get_dish_summary_by_tag(t_.id)
        selection_ = random.choice(dishs_)
        re_service.save_changes(Recommendation(
            user_id=user_id,
            dish_id=selection_.id,
            tag_id=t_.id,
            created_at=date.today(),
            updated_at = date.today(),
        ))
    return


def other_candidate(today_recommendations, n_dishs_limit=30):

    candidate_cards = {}
    candidate_cards['cards'] = []
    for tag_ in [r[2] for r in today_recommendations]:
    ## search tag , 1 tag for 1 card
    ## search dishs, build a card
        dishs = dish_service.get_dish_summary_by_tag(tag_.id)
        n_dishs = len(dishs)

        card = {}
        card['dish_type_id'] = CARD_TYPE_CODE.SMALL_IMAGE
        card['dish_type_name'] = tag_.tagname
        card['dish_count'] = n_dishs if n_dishs < n_dishs_limit else n_dishs_limit
        card['dish'] = []

        for dish_idx_, dish_ in enumerate(dishs):
            if dish_idx_ > n_dishs_limit-1:
                break
            dish = {}
            dish['dish_id'] = dish_.id
            dish['dish_name'] = dish_.dishname
            dish['dish_image_link'] = dish_.dish_image_link
            card['dish'].append(dish)

        assert len(card['dish']) <= n_dishs_limit, 'n_dishs_limit not work'
        candidate_cards['cards'].append(card)
    return candidate_cards