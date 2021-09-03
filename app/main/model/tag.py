from .. import db, flask_bcrypt



class Tag(db.Model):
    """
    dish to tag is many to many
    {
        'dish_id':123,
        'tags': ['香', '下午茶', '一家三口', '烤', '烘焙'],
    }
    """
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tagname = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return "<Tag '{}'>".format(self.tagname)