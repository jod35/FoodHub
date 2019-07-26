from foodhub import db

class Food(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False,unique=True)
    unit=db.Column(db.String,nullable=False)
    stock=db.Column(db.String,nullable=False)
    price=db.Column(db.String,nullable=False)
    item_type=db.Column(db.String,nullable=False)
    descrition=db.Column(db.String,nullable=False)
    image_url=db.Column(db.String,nullable=False)

    def __repr__(self):
        return '<name={}, price={}>'.format(self.name,self.price)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,nullable=False)
    email=db.Column(db.String,nullable=False)
    password=db.Column(db.String,nullable=False)

    def __repr__(self):
        return '<name ={},email={}>'.format(self.name,self.email)



