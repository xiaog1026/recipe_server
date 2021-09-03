from .. import db, flask_bcrypt

class Step(db.Model):
    """
    dish to step is 1 to many
    example
    {
        'step_description': '先把海苔用剪刀剪碎，海苔可以剪的碎一些，方便压模。',
        'step_image': 'https://cp1.douguo.com/upload/caiku/0/8/a/200_08da2df32fd43405ac0ff921d4ee55ba.jpeg'
    }
    """
    __tablename__ = "step"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    step_no = db.Column(db.Integer, nullable=False)
    step_description = db.Column(db.String(50), nullable=False)
    step_image_link = db.Column(db.String(200), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))


    def __repr__(self):
        return "<Dish '{}' Step '{}'>".format(self.dish_id, self.step_description)