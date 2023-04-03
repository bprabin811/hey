from flask import Flask, render_template,request
from pymongo import MongoClient

client = MongoClient('mongodb+srv://prabin:bprabin@cluster0.2phmxej.mongodb.net/test')
db = client['pro']


app = Flask(__name__,static_folder='static',template_folder='templates')
insta ='https://www.instagram.com/pro_win811'
github='https://github.com/bprabin811'
fb='https://www.facebook.com/pro.win.125'
snap='https://www.snapchat.com/add/prabin_bhatta19?share_id=eOmfcJXkYcQ&locale=en-US'
tocall="tel:+9779869908380"
tomail="mailto:bprabin811@gmail.com"

@app.route("/")
def hello_world():
    return render_template('index.html',insta=insta,github=github,fb=fb,snap=snap,tocall=tocall,tomail=tomail)


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
    return render_template('index.html',insta=insta,github=github,fb=fb,snap=snap,tocall=tocall,tomail=tomail)