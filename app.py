from flask import Flask, render_template,request
from pymongo import MongoClient
from PIL import Image
import base64
import io
# from db import retrive_data

client = MongoClient('mongodb+srv://prabin:bprabin@cluster0.2phmxej.mongodb.net/test')
db = client['pro']

name=[
    "KidzWorld: Learn With Fun",
    "Helix-Infinite",
    "ImageLab-AI: Image Colorization using CNN",
    "Multi-Store E-mart for Vegetables",
    "Depression Analysis using Chatbot",
    "Churn Prediction System",
]
app = Flask(__name__,static_folder='static',template_folder='templates')

items=[]

@app.route("/")
def hello_world():
    try:
        items.clear()
        for i in range(len(name)):
            image_data = db.mydatabse.find_one({'name': name[i]})['image_data']
            project_link=db.mydatabse.find_one({'name': name[i]})['link']
            project_type=db.mydatabse.find_one({'name': name[i]})['type']
            image = Image.open(io.BytesIO(image_data))
            img_io = io.BytesIO()
            image.save(img_io, format='PNG')
            img_io.seek(0)
            img_str = base64.b64encode(img_io.getvalue()).decode()

            if project_type == 'app':
                actionType = 'Download'
            elif project_type == 'game':
                actionType = 'Download'
            else:
                actionType = 'View Project'

            item = {
                'image': img_str,
                'name': name[i],
                'action': actionType,
                'link': project_link,
            }
            items.append(item) 
        return render_template('index.html',items=items)
    except:
        return '<p> Something Went Wrong, Please try again later.</p>'
                            


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