from flask import Flask, render_template, request, jsonify, url_for
import io, sys

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
    return render_template('exercises.html')
    
@app.route('/exercises/1')
def excercise1():
    return render_template('ex1.html', print_button=True, assign_vars=False, list_button=False)


@app.route('/exercises/2')
def excercise2():
    return render_template('code.html', print_button=False, assign_vars=True, list_button=False)


@app.route('/exercises/3')
def excercise3():
    return render_template('ex3.html', print_button=False, assign_vars=False, list_button=True)


last = []


@app.route('/process_print', methods=['POST'])
def process_print():
    global last
    data = request.get_json()  # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    last.append("print(" + value + ")")
    result = '<br />'.join(str(x) for x in last)
    return jsonify(result=result)  # return the result to JavaScript

last2 = []
last_scaled = []


@app.route('/process_assign', methods=['POST'])
def process_assign():
    global last_scaled
    data = request.get_json()  # retrieve the data sent from JavaScript
    # process the data using Python code
    value = data['value']
    var_name = data['var']
    last2.append(var_name + " = " + value)
    last_scaled.append(var_name + " = 100*(" + value + ")")
    result = '<br />'.join(str(x) for x in last2)
    return jsonify(result=result)  # return the result to JavaScript

last3 = []

@app.route('/process_list_assign', methods=['POST'])
def process_list_assign():
    global last3
    data = request.get_json()  # retrieve the data sent from JavaScript
    # process the data using Python code
    print("aaaaaa")
    value = data['value']
    var_name = data['var']
    last3.append(var_name + " = [" + value + "]")
    result = '<br />'.join(str(x) for x in last3)
    return jsonify(result=result)  # return the result to JavaScript


index = 0


@app.route('/process_list_access', methods=['POST'])
def process_list_access():
    global last3
    global index
    data = request.get_json()  # retrieve the data sent from JavaScript
    # process the data using Python code
    list_name = data['listName']
    var_name = data['var']
    index_val = data['index']
    last3.append(var_name + " = " + list_name + "[" + index_val + "]")
    index = int(index_val)
    result = '<br />'.join(str(x) for x in last3)
    return jsonify(result=result)  # return the result to JavaScript


x = 0
y = 4


@app.route('/process_code', methods=['POST'])
def process_code():
    global last2
    global x
    global y
    print("yooooo")
    last_editted = []
    last_editted.insert(0, "x=" + str(x))
    last_editted.insert(0, "y=" + str(y))
    for elem in last_scaled:
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
    y = 400 - loc['y']
    print(result)
    return jsonify(result=result, result_x=x, result_y=y)  # return the result to JavaScript


@app.route('/process_code_list', methods=['POST'])
def process_code_list():
    global last3
    global index
    last_editted = []
    last_editted.insert(0, "val=None")
    for elem in last3:
        last_editted.append(elem)
    for i in range(5):
        last_editted.append('l' + str(i) + ' = my_list[' + str(i) + '] if len(my_list) > ' + str(i) + ' else ""')
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

    x_coor = 100 * index
    val = loc['val']
    l0 = loc['l0']
    l1 = loc['l1']
    l2 = loc['l2']
    l3 = loc['l3']
    l4 = loc['l4']
    print(val)
    return jsonify(result=result, result_x=x_coor, result_val=val, l0=l0, l1=l1, l2=l2, l3=l3,
                   l4=l4)  # return the result to JavaScript


@app.route('/process_code_print', methods=['POST'])
def process_code_print():
    global last
    print("Hello")
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
    print(result)
    return jsonify(result=result)  # return the result to JavaScript


@app.route('/process_del', methods=['POST'])
def process_del():
    global last
    if last:
        last.pop()
    if last:
        result = '<br />'.join(str(x) for x in last)
    else:
        result = ""
    return jsonify(result=result)  # return the result to JavaScript

@app.route('/process_del2', methods=['POST'])
def process_del2():
    global last2
    global last_scaled
    if last2 and last_scaled:
        last2.pop()
        last_scaled.pop()
    if last2:
        result = '<br />'.join(str(x) for x in last2)
    else:
        result = ""
    return jsonify(result=result)  # return the result to JavaScript

@app.route('/process_del3', methods=['POST'])
def process_del3():
    global last3
    if last3:
        last3.pop()
    if last3:
        result = '<br />'.join(str(x) for x in last3)
    else:
        result = ""
    return jsonify(result=result)  # return the result to JavaScript


@app.route('/monkey')
def monkey():
    monkey_position = {'x': 0, 'y': 0}
    return render_template('index.html', monkey_position=monkey_position)
