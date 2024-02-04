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
    return render_template('code.html', print_button=True, assign_vars = False, list_button = False)

@app.route('/2')
def excercise2():
    return render_template('code.html', print_button=False, assign_vars = True, list_button = False)

@app.route('/3')
def excercise3():
    return render_template('code.html', print_button=False, assign_vars = False, list_button = True)

last = []

@app.route('/process_print', methods=['POST'])
def process_print():
    global last
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    last.append("print(" + value + ")")
    result = '<br />'.join(str(x) for x in last)
    return jsonify(result=result) # return the result to JavaScript

@app.route('/process_assign', methods=['POST'])
def process_assign():
    global last
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    var_name = data['var']
    last.append(var_name + " = " + value)
    result = '<br />'.join(str(x) for x in last)
    return jsonify(result=result) # return the result to JavaScript

@app.route('/process_list_assign', methods=['POST'])
def process_list_assign():
    global last
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    var_name = data['var']
    last.append(var_name + " = [" + value + "]")
    result = '<br />'.join(str(x) for x in last)
    return jsonify(result=result) # return the result to JavaScript

x = 0
y = 0

result = "Syntax Error"
@app.route('/process_code', methods=['POST'])
def process_code():
    global last
    global x
    global y
    last_editted = []
    last_editted.insert(0, "x=" + str(x))
    last_editted.insert(0, "y=" + str(y))
    for elem in last:
        last_editted.append(elem)
    code = "\n".join(last_editted)
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    loc = {}
    try: 
        exec(code, globals(), loc)
        result = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
    except:
        result = "Syntax Error"

    x = loc['x']
    y = loc['y']
    return jsonify(result = result, result_x=x, result_y=y) # return the result to JavaScript

@app.route('/process_del', methods=['POST'])
def process_del():
    global last
    if last:
        last.pop()
    if last:
        result = '<br />'.join(str(x) for x in last)
    else:
        result = ""
    return jsonify(result=result) # return the result to JavaScript

@app.route('/monkey')
def monkey():
    monkey_position = {'x': 0, 'y': 0}
    return render_template('index.html', monkey_position=monkey_position)


@app.context_processor
def coordinate_processor():
    global monkey_x
    def return_x():
        return monkey_x
    def return_y():
        return monkey_y
    return dict(return_x=return_x, return_y=return_y)