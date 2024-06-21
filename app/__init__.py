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
    hobbies_list = ['Reading', 'Hiking', 'Programming', 'Photography']
    return render_template('multi_items.html', title="Hobbies", items=hobbies_list)

@app.context_processor
def inject_pages():
    return dict(pages=pages)