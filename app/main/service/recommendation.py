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
from datetime import datetime, date, timezone
from app.main.util.constant import *
import random
from sqlalchemy.sql import func

def get_today_recommendation(user_id):
    return db.session.query(Recommendation,Dish,Tag).join(Dish).join(Tag).filter(Recommendation.user_id==user_id, Recommendation.created_at >= date.today()).all()

def save_changes(data):
    db.session.add(data)
    db.session.commit()

