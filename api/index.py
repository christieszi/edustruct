from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/excercise')
def excercise():
    return render_template('code.html')