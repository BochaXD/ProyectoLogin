from flask import Flask,render_template
import pymongo
app=Flask(__name__)
#ROuter
from users import routes
#database
client=pymongo.MongoClient()
db=client.user_login_system

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup/')
def dashboard():
    return render_template('signup.html')