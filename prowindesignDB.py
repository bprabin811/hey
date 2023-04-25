import pymongo
import io
from PIL import Image

# Connect to the MongoDB server
client = pymongo.MongoClient("mongodb+srv://prabin:bprabin@cluster0.2phmxej.mongodb.net/test")

# Select the database
db = client["ProwinDesigns"]

# Select the collection
# collection = db["projects"]

collection = db["appdesigns"]



imageLink=['hey\\images\\shopping_app.png','hey\\images\\shoppy _app.png','hey\\images\\compass.png']
image_data=[]

# Define the image data
for i in range(len(imageLink)):
    with Image.open(imageLink[i]) as image:
        img_io = io.BytesIO()
        image.save(img_io, format='PNG')
        img_io.seek(0)
        image_data.append(img_io.read())

# Define the data to be added
# data = [
#     {
#         "title": "ImageLab-AI: Image Colorization using CNN",
#         "image": image_data[0],
#         "type": "Project",
#         "link": "https://github.com/bprabin811/Imagelab-AI",
#         "action": "View",
#         "language":"Python/HTML/CSS/JS"
#     },
#     {
#         "title": "Multi-Store E-mart for Vegetables",
#         "image": image_data[1],
#         "type": "Project",
#         "link": "https://github.com/bprabin811/emarket",
#         "action": "View",
#         "language":"HTML/CSS/PHP"
#     },
#     {
#         "title": "KidzWorld: Learn With Fun",
#         "image": image_data[2],
#         "type": "Project",
#         "link": "https://github.com/bprabin811/kidzword-Learn-with-fun/releases/download/v1.1.0/app-release.apk",
#         "action": "Download",
#         "language":"Flutter"
#     }
# ]


data=[
  {
    "title": "Shopping Store App",
    "image": image_data[0],
    "link": "https://github.com/bprabin811/Shopping-Store",
    "action": "View Code",
    "date": "March 5",
    "type": "app",
    "language": "Flutter"
  },
  {
    "title": "HomePage for ecommerce App",
    "image": image_data[1],
    "link": "https://github.com/bprabin811/Shoppy-A-MarketPlace",
    "action": "View Code",
    "date": "March 16",
    "type": "app",
    "language": "Flutter"
  },
  {
    "title": "Compass Using Flutter",
    "image": image_data[2],
    "link": "https://github.com/bprabin811/Compass",
    "action": "View Code",
    "date": "Feb 18",
    "type": "app",
    "language": "Flutter"
  }
]


# Insert the data into the collection
result = collection.insert_many(data)

# Print the IDs of the inserted documents
print(result.inserted_ids)
