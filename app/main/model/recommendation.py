from .. import db, flask_bcrypt
from datetime import datetime
from sqlalchemy.sql import func

class Recommendation(db.Model):
    """

    """
    __tablename__ = "recommendation"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))
    created_at = db.Column(db.DateTime, nullable=False, default=func.now())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.now())

    def __repr__(self):
        return "<User '{}' dish '{}'>".format(self.user_id, self.dish_id)