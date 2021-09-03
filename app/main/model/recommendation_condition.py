from .. import db, flask_bcrypt
from datetime import datetime
from sqlalchemy.sql import func

class RecommendationCondition(db.Model):
    """

    """
    __tablename__ = "recommendation_condition"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    condition_name = db.Column(db.String(200))
    condition_code = db.Column(db.Integer)
    condition_scope_name = db.Column(db.String(200))
    condition_scope_code = db.Column(db.Integer)
    condition_value = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return "<User '{}' scope '{}' condition '{}'>".format(self.user_id, self.condition_scope_name, self.condition_name)