from flask import Flask, render_template, url_for

app = Flask(__name__, static_url_path='/static')
# replace the name of the app with the name of our app
app.config['APP_NAME'] = 'EduStruct'

@app.route('/index')
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/exercises')
def exercises():
    return render_template('exercise.html')