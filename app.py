from flask import Flask, render_template,request
from pymongo import MongoClient
from PIL import Image
import base64
import json
import io
from flask import Flask, jsonify
import json
from bson import ObjectId
from flask_cors import CORS
import openai


client = MongoClient('mongodb+srv://prabin:bprabin@cluster0.2phmxej.mongodb.net/test')
db = client['pro']

# Select the database
db_prowin = client["ProwinDesigns"]

# Select the collection
collection = db_prowin["projects"]
appdesigns_collection=db_prowin["appdesigns"]
webdesigns_collection=db_prowin["webdesigns"]

app = Flask(__name__,static_folder='static',template_folder='templates')
# CORS(app, origins=['https://bprabin.com.np'])
CORS(app, origins=['http://uiboxx.in'])


@app.route('/projects')
def get_data():
    data = collection.find()
    result = []
    for doc in data:
        # Convert ObjectId to string
        doc["_id"] = str(doc["_id"])
        # Encode binary data as Base64
        if "image" in doc:
            doc["image"] = base64.b64encode(doc["image"]).decode("utf-8")
        result.append(doc)
    json_data = json.dumps(result)
    return json_data


# ---------------------------

# Set your OpenAI API key
openai.api_key = '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'

@app.route('/generate-code', methods=['GET'])
def generate_profile_card():
    prompt_text = request.args.get('prompt', ''+' write HTML and CSS in same file index.html')

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt_text,
        max_tokens=2500
    )

    generated_text = response.choices[0].text.strip()
    return jsonify({'gen_code': generated_text})

# def generate_response(prompt):
#     response = openai.Completion.create(
#         engine='text-davinci-003',  # Choose the most suitable engine for your use case
#         prompt=prompt,
#         max_tokens=500  # Specify the maximum length of the generated response
#     )

#     generated_text = response.choices[0].text.strip()
#     return generated_text

# # Example usage
# prompt_text = "can you make a beautiful profile card using html and css?"
# generated_response = generate_response(prompt_text)
# print(generated_response)

# ---------------------------


@app.route('/webdesigns')
def get_webdesigns_data():
    data = webdesigns_collection.find()
    result = []
    for doc in data:
        # Convert ObjectId to string
        doc["_id"] = str(doc["_id"])
        # Encode binary data as Base64
        if "image" in doc:
            doc["image"] = base64.b64encode(doc["image"]).decode("utf-8")
        result.append(doc)
    json_data = json.dumps(result)
    return json_data


@app.route('/appdesigns')
def get_appdesigns_data():
    data = appdesigns_collection.find()
    result = []
    for doc in data:
        # Convert ObjectId to string
        doc["_id"] = str(doc["_id"])
        # Encode binary data as Base64
        if "image" in doc:
            doc["image"] = base64.b64encode(doc["image"]).decode("utf-8")
        result.append(doc)
    json_data = json.dumps(result)
    return json_data


# @app.route('/appdesigns/<string:id>/likes', methods=['PUT'])
# def update_design_likes(id):
#     # Find the design by its ID
#     design = appdesigns_collection.find_one({"id": id})
#     if design:
#         # Get the new likes count from the request body
#         likes = request.json.get('likes', None)
#         if likes is not None:
#             # Update the likes count in the design object
#             design['likes'] = likes
#             # Update the design in the database
#             appdesigns_collection.update_one({"id": id}, {"$set": design})
#             return jsonify({"message": "Likes updated successfully"})
#         else:
#             return jsonify({"message": "Likes count not found in request body"}), 400
#     else:
#         return jsonify({"message": "Design not found"}), 400


name=[
    "KidzWorld: Learn With Fun",
    "Helix-Infinite",
    "ImageLab-AI: Image Colorization using CNN",
    "Multi-Store E-mart for Vegetables",
    "Depression Analysis using Chatbot",
    "Churn Prediction System",
]



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

    return '<p>Form submitted Successfully.</p>'





