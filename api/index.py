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
    return render_template('visualisation.html', printed_texts='')

last = []

@app.route('/process_print', methods=['POST'])
def process():
    global last
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    last.append("print(" + value + ")")
    result = '<br />'.join(str(x) for x in last)
    return jsonify(result=result) # return the result to JavaScript

@app.route('/process_code', methods=['POST'])
def process_code():
    global last
    code = "\n".join(last)
    print("Code = " + code)
    result = eval(code)
    return jsonify(result=result) # return the result to JavaScript