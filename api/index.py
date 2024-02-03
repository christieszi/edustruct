from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
# replace the name of the app with the name of our app
app.config['APP_NAME'] = 'EduStruct'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/exercises')
def excercises():
    return render_template('exercise.html')