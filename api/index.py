from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello peasants :)'

@app.route('/about')
def about():
    return 'About'