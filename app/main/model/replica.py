from .. import db, flask_bcrypt

class Replica(db.Model):
    """
    dish to Replica is 1 to many
    example
    'more_replica': [
        {'replica_href': 'https://www.douguo.com/dish/28227282',
        'replica_image_href': 'https://cp1.douguo.com/upload/note/7/3/5/320_73acc572f545202cac9a9affac1f8245.jpeg',
        'replica_user_href': 'u73831737479915',
        'replica_user_name': '张冰ihej',
        'replica_user_id': 'u73831737479915',
        'replica_user_comment': '海苔碎饭团'},
        {'replica_href': 'https://www.douguo.com/dish/28098324',
        'replica_image_href': 'https://cp1.douguo.com/upload/note/b/a/0/320_ba4fc24662a319ef62834e92580c4090.jpeg',
        'replica_user_href': 'u87319257111456',
        'replica_user_name': '尘尘宝宝敲可爱',
        'replica_user_id': 'u87319257111456',
        'replica_user_comment': '吼吼吃啊'},
        {'replica_href': 'https://www.douguo.com/dish/25684325',
        'replica_image_href': 'https://cp1.douguo.com/upload/note/6/f/8/320_6f4baed1fcb74273ed9d0a96b3768f48.jpeg',
        'replica_user_href': 'u06176778386439',
        'replica_user_name': '火龙果的豆芽菜',
        'replica_user_id': 'u06176778386439',
        'replica_user_comment': ''}],
    """
    __tablename__ = "replica"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    replica_href = db.Column(db.String(50), nullable=False)
    replica_image_href = db.Column(db.String(200), nullable=False)
    comment = db.Column(db.String(200), nullable=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Dish '{}' Replica '{}'>".format(self.dish_id, self.comment)