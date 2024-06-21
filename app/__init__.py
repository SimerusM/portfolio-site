import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# List of pages, update this list for dynamic page adding
pages = [
    {'name': 'Home', 'endpoint': 'index'},
    {'name': 'Hobbies', 'endpoint': 'hobbies'}
]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbies():
    # Next step, create a specific hobbies file to read from
    hobbies_list = ['Reading', 'Hiking', 'Programming', 'Photography']
    hobbies_images = [
        './static/img/hobby1.jpg',
        './static/img/hobby1.jpg',
        './static/img/hobby1.jpg',
        './static/img/hobby1.jpg'
    ]
    return render_template('multi_items.html', title="Hobbies", items=hobbies_list, images=hobbies_images)

@app.context_processor
def inject_pages():
    return dict(pages=pages)