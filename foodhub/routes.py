from foodhub import app
from foodhub.models import User,Food
from flask import render_template,redirect,request,session,url_for


@app.route('/')
def index():
    foods=Food.query.all()
    return render_template('index.html',foods=foods)