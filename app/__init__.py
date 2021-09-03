# app/__init__.py

from flask_restx import Api
from flask import Blueprint

from .main.controller._user import api as user_ns
from .main.controller._tag import api as tag_ns
from .main.controller._step import api as step_ns
from .main.controller._replica import api as replica_ns
from .main.controller._ingredient import api as ingredient_ns
from .main.controller._dish import api as dish_ns
from .main.controller._comment import api as comment_ns
from .main.controller.card import api as card_ns
from .main.controller.table import api as table_ns
from .main.controller._recommendation_condition import api as recommendation_condition_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(tag_ns, path='/tag')
api.add_namespace(step_ns, path='/step')
api.add_namespace(replica_ns, path='/replica')
api.add_namespace(ingredient_ns, path='/ingredient')
api.add_namespace(dish_ns, path='/dish')
api.add_namespace(comment_ns, path='/comment')
api.add_namespace(recommendation_condition_ns, path='/recommendation_condition')
# api.add_namespace(recommendation_ns, path='/recommendation')

api.add_namespace(card_ns, path='/card')
api.add_namespace(table_ns, path='/table')
