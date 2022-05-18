from crypt import methods
from flask import Flask,render_template
from login import app
from users.models import User

@app.route('/user/signup',methods=['POST'])
def signup():

    return User().signup()