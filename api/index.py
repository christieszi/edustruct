from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('welcome-page.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/exercises')
def excercises():
    return render_template('exercises.html')