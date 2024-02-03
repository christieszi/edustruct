import re
import io
import sys

from printing_problems import *

def evaluate_code(code):
    #Checks excution
    try:
        exec(code)
    except Exception as e:
        print("Execution error! Please check your Code")
        return e
    return None


def capture_output(func):
    # Output of a function
    buffer = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = buffer
    func()
    sys.stdout = old_stdout
    return buffer.getvalue()


# get the string of the block the user has chosen
def get_block_string():
    # returns list of block strings
    pass



#This only works for 1 Block however some challanges will have more than 1
def replace_code_with_blocks(problem):
    # replace block with result from get_block_string while loop?
    code = ""
    l = 0
    r = 5
    
    while r < len(problem):
        if problem[l:r] != "block":
            code += problem[l]
            l += 1
            r += 1
        else:
            code += get_block_string()[0]
            l += len(get_block_string()[0])
            r += len(get_block_string()[0])
            # remove first element from list
            get_block_string().pop(0)
    return code

def test(problem):
    code = replace_code_with_blocks(problem)
    return evaluate_code(code)

# unit tests
def test_evaluate_code():
    assert capture_output(test(user_problem1)) == "Hello world"
    assert capture_output(test(user_problem2))== "John\nAdam"
    assert capture_output(test(user_problem3)) == "Harry\n25"
    assert capture_output(test(user_problem4)) == "full name: Adam Smith"
    assert matches_regex(capture_output(test(user_problem5)), r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$")

def matches_regex(string, regex):
    #Validation test
    return bool(re.match(regex, string))


