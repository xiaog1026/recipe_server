import uuid
import datetime

from app.main import db
from app.main.model.dish import Dish, dish_m2m_tag
from app.main.model.tag import Tag
from app.main.service import tag as tag_service
from app.main.service import user as user_service
from app.main.service import comment as comment_service
from app.main.service import replica as replica_service
from app.main.util.constant import *
from app.main.service import dish as dish_service
from app.main.service import tag as tag_service
import random
import logging
import pandas as pd

logger = logging.getLogger('card service')


def get_cards(card_page, n_cards, n_dishs_limit):
    cards = {}
    cards['cards'] = []
    ## search tag , 1 tag for 1 card
    tags = tag_service.get_tag_page(card_page, n_cards)
    for tag_ in tags.items:
        ## search dishs, build a card
        dishs = dish_service.get_dish_summary_by_tag(tag_.id)
        n_dishs = len(dishs)

        card = {}
        card['dish_type'] = random.choice(CARD_TYPE.LIST)
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
        cards['cards'].append(card)
    return cards

# def get_recommendation_card(user_id, conditions):
#
#     condition_df = pd.DataFrame([c.__dict__ for c in conditions])
#     n_dishs = condition_df[condition_df['condition_scope_name']=='n_dishs']['condition_value'].values[0]
#
#
#     tags = tag_service.get_tags()
#     recommendations = []
#     for t_ in random.sample(tags, n_dishs):
#         dishs_ = dish_service.get_dish_summary_by_tag(t_.id)
#         selection_ = random.choice(dishs_)
#         recommendations.append({'tag_id':t_.id, 'tag_id':t_.tagname, 'dish_id':selection_.id, 'dish_name':selection_.dishname, 'dish_image_link':selection_.dish_image_link})
#
#     output = {
#       "dish_count": len(recommendations),
#       "dish": recommendations,
#     }
#
#     return output

def save_changes(data):
    db.session.add(data)
    db.session.commit()