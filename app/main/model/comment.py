from .. import db, flask_bcrypt

class Comment(db.Model):
    """
    dish to comment is 1 to many
    'comment': [{'user': '花好月圆128',
       'comment_content': '动手的乐趣',
       'comment_date': '2020-05-19',
       'herf': 'https://www.douguo.com/u/u26163545.html'}],
    """
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(200))
    comment_date = db.Column(db.DateTime)
    user_herf = db.Column(db.String(200))
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


    def __repr__(self):
        return "<Dish '{}' Comment '{}'>".format(self.dish_id, self.comment)