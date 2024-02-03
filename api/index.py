from flask import Flask, render_template, request, jsonify
import io, sys

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello peasants :)'

@app.route('/about')
def about():
    return 'About'

@app.route('/exercise')
def exercise():
    return render_template('code.html')

@app.route('/game')
def game():
    return render_template('index.html')

last = []

@app.route('/process_print', methods=['POST'])
def process():
    global last
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    last.append(value)
    result = '<br />'.join(str(x) for x in last)
    return jsonify(result=result) # return the result to JavaScript


@app.route('/process_code', methods=['POST'])
def process_code():
    global last
    code = "\n".join(last)
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    exec(code)
    result = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return jsonify(result=result) # return the result to JavaScript