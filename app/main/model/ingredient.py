from .. import db, flask_bcrypt

class Ingredient(db.Model):
    """
    dish to ingredient is 1 to many
    example
    {'ingredent_name': '低筋面粉', 'ingredent_weight': '90克'}
    """
    __tablename__ = "ingredient"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredientname = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.String(50), nullable=False)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'))


    def __repr__(self):
        return "<Dish '{}' Ingredient '{}'>".format(self.dish_id, self.ingredientname)