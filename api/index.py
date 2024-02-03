from flask import Flask, render_template, request, jsonify

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
    return render_template('visualisation.html')

last = []
@app.route('/process', methods=['POST'])
def process():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    last.append(data)
    result = last
    return jsonify(result=result) # return the result to JavaScript