from flask import Flask, render_template, request, jsonify
import io, sys

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello peasants :)'

@app.route('/about')
def about():
    return 'About'

@app.route('/1')
def excercise1():
    return render_template('code.html', print_button=True)

@app.route('/2')
def excercise2():
    return render_template('code.html', print_button=False)

@app.route('/TESTINO')
def TESTINO():
    return render_template('TESTINO.html')

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

result = "Syntax Error"
@app.route('/process_code', methods=['POST'])
def process_code():
    global last
    code = "\n".join(last)
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    try: 
        exec(code)
        result = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    except:
        result = "Syntax Error"

    
    return jsonify(result=result) # return the result to JavaScript