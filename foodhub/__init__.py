from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app=Flask(__name__)
app.config['SECRET_KEY']="SADSGHD9SD89AS7DAD09@@3E34"
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///food.db"

db=SQLAlchemy(app)
migrate=Migrate(app,db)


