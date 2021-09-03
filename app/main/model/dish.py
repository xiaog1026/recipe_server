from .. import db, flask_bcrypt

dish_m2m_tag = db.Table('dish_m2m_tag',
                            db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
                            db.Column('dish_id', db.Integer, db.ForeignKey('dish.id'), primary_key=True)
                            )

class Dish(db.Model):
    """
    user to dish is 1 to many
    example
    {'dish_href': 'https://www.douguo.com/cookbook/2491724.html',
     'dish_id': '2491724',
     'dish_image_link': 'https://cp1.douguo.com/upload/caiku/2/b/4/690x390_2b66746488cd5ed42ad02e438353b104.jpeg',
     'dish_name': '鱼松海苔饼干',
     'dish_vedio_link': 'https://vplay.douguo.com/lknGmlMr_ixer7Xc3mPNcjaG41tp_DgUO__640x362.mp4',
     'author': '壹日壹记',
     'author_comment': '家里还有一些鱼松跟海苔干脆就用它来做款咸味的小饼干吧，制作过程也非常简单，家里有小朋友的也可以带上小朋友一起来场亲子互动，喜欢的小伙伴可以在家试试。',
     'view': '13.5万',
     'favorite': '2964',
     'ingredents': [{'ingredent_name': '低筋面粉', 'ingredent_weight': '90克'},
      {'ingredent_name': '糖粉', 'ingredent_weight': '15克'},
      {'ingredent_name': '鱼松', 'ingredent_weight': '8克'},
      {'ingredent_name': '全蛋液', 'ingredent_weight': '20克'},
      {'ingredent_name': '海苔', 'ingredent_weight': '12克'},
      {'ingredent_name': '黄油', 'ingredent_weight': '40克'}],
     'steps': [{'step_description': '先把海苔用剪刀剪碎，海苔可以剪的碎一些，方便压模。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/0/8/a/200_08da2df32fd43405ac0ff921d4ee55ba.jpeg'},
      {'step_description': '把黄油提前称好重，放至室温软化成膏状。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/4/a/a/200_4a55a6b61d22af71e09d7afe5b11319a.jpeg'},
      {'step_description': '黄油软化好以后放入打蛋盆，筛入糖粉，先用刮刀搅至无干粉状。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/8/0/d/200_809b430f5b2fc64f7fbfbc3b322444ad.jpeg'},
      {'step_description': '用蛋抽或电动打蛋器搅打至黄油颜色变浅，体积蓬松。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/4/0/b/200_40048057285a241294cda8ed5720e1cb.jpeg'},
      {'step_description': '分2次加入过筛的面粉，搅拌至无干粉状。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/a/6/d/200_a63f49060aa95d0f1e8213c3ff363fbd.jpeg'},
      {'step_description': '放入海苔碎、鱼松跟蛋液。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/6/7/8/200_6717eae2b82169c6b7caf6354215d5d8.jpeg'},
      {'step_description': '揉成面团。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/4/e/4/200_4ee2d937ef458cf54ad0853cf0906c44.jpeg'},
      {'step_description': '把揉好的面团放在2张吸油纸中间，用擀面杖擀成约0.4CM的薄片。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/2/8/d/200_28323ce67b4dad200a0da3f0fef2188d.jpeg'},
      {'step_description': '用饼干模具压出生胚，剩下的面团继续揉成面团擀薄，压出生胚。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/9/6/0/200_96554a294dfaeaf3df3ee1bd330ff5c0.jpeg'},
      {'step_description': '烤盘铺一张吸油纸，放入做好的饼干生胚，用叉子在上面扎几个孔，避免在烤制过程中鼓包。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/9/3/b/200_937b34aab670615a596c52f9f0158b6b.jpeg'},
      {'step_description': '烤箱提前预热，上：150、下：130，烤制20分钟，时间跟温度需根据自己家烤箱自行调整。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/2/5/8/200_257ffc4abeaaefdf4efb3ae4740182a8.jpeg'},
      {'step_description': '烤完后放入烤网自然冷却后，饼干就酥了。一次吃不完可以放入饼干盒。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/9/7/9/200_974d61ebca2616c693bd19662394aa89.jpeg'},
      {'step_description': '里面加了熟的芝麻吃起来特别香，偶尔拿它磨磨牙非常不错哦。',
       'step_image': 'https://cp1.douguo.com/upload/caiku/d/f/4/200_df64b82c531b5474d16661db85c34f74.jpeg'}],
     'tip': '1、这是一款咸味的小饼干，黄油要提前软化成膏状。 2、糖粉跟面粉提前过筛，去掉里面的颗粒。 3、面团如果干就多加点蛋液，如果太软可以包上保鲜膜放入冰箱冷藏一下。 4、面团放在2张吸油纸中间可以方便擀制。 5、上面要用叉子扎孔，避免烤制过程中鼓包。 6、不同品牌的烤箱不同，烤制时间及温度需要根据自己家的烤箱脾气自行调整。\n做菜好吃都有技巧，我的每道菜都有小妙招，大家搜索“豆果”可以直接查看我的菜谱！',
     'tags': [],
     'more_other_recipe_href': 'https://www.douguo.com/caipu/%E9%B1%BC%E6%9D%BE%E6%B5%B7%E8%8B%94%E9%A5%BC%E5%B9%B2',
     'more_replica_href': '',
     'more_relative_recommendaton_href': 'https://www.douguo.com/caipu/%E9%B1%BC%E6%9D%BE%E6%B5%B7%E8%8B%94%E9%A5%BC%E5%B9%B2',
     'comment': [{'user': '花好月圆128',
       'comment_content': '动手的乐趣',
       'comment_date': '2020-05-19',
       'herf': 'https://www.douguo.com/u/u26163545.html'}],
     'more_other_recipe': [{'dish_name': '#美食视频挑战赛#鱼松海苔饼干',
       'dish_id': '2491724',
       'dish_herf': 'https://www.douguo.com/cookbook/2491724.html'},]

    """
    __tablename__ = "dish"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.Integer, unique=True, nullable=False)
    dishname = db.Column(db.String(50), nullable=False)
    view = db.Column(db.Integer, nullable=False)
    favorite = db.Column(db.Integer, nullable=False)
    dish_image_link = db.Column(db.String(200), nullable=False)
    dish_vedio_link = db.Column(db.String(200), nullable=False)
    dish_link = db.Column(db.String(200), nullable=False)
    author_comment = db.Column(db.String(200))
    tip = db.Column(db.String(200))
    more_other_recipe_href = db.Column(db.String(200), nullable=False)
    more_replica_href = db.Column(db.String(200), nullable=False)
    more_relative_recommendaton_href = db.Column(db.String(200), nullable=False)
    tags = db.relationship('Tag', secondary=dish_m2m_tag, lazy='subquery', backref=db.backref('dishes', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Dish '{}'>".format(self.dishname)