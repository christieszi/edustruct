from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello peasants :)'

@app.route('/about')
def about():
    return 'About'

@app.route('/excercise')
def excercise():
    return render_template('code.html')

@app.route('/game')
def game():
    return render_template('index.html')

@app.route('/visual')
def visual():
    return render_template('visualisation.html', printed_text="")

@app.route('/print_text', methods=['POST'])
def print_text():
    button_text = request.form['button_text']
    current_text = request.form['current_text']
    printed_texts = current_text + " new line print(" + button_text + ")"
    return render_template('visualisation.html', printed_text=printed_texts)