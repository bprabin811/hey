from flask import Flask, render_template,request
from pymongo import MongoClient

client = MongoClient('mongodb+srv://prabin:bprabin@cluster0.2phmxej.mongodb.net/test')
db = client['pro']


app = Flask(__name__,static_folder='static',template_folder='templates')


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # save the form data to the MongoDB database
    db.pro.insert_one({
        'name': name,
        'email': email,
        'message': message
    })
    return render_template('index.html')