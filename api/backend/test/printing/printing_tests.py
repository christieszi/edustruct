import re
import io
import sys

from printing_problems import *

def evaluate_code(code):
    try:
        exec(code)
    except Exception as e:
        print("error in code")
        return e
    return None


def capture_output(func):
    # Create a string buffer
    buffer = io.StringIO()
    # Save the current stdout (usually the terminal/screen)
    old_stdout = sys.stdout
    # Redirect stdout to the buffer
    sys.stdout = buffer
    # Call the function
    func()
    # Restore the original stdout
    sys.stdout = old_stdout
    # Return what was captured
    return buffer.getvalue()


# get the string of the block the user has chosen
def get_block_string():
    # returns list of block strings
    pass

def replace_code_with_blocks(problem):
    # replace block with result from get_block_string
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
    # pattern = r"^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$"
    return bool(re.match(regex, string))

#^[\w'\-,.][^0-9_!¡?÷?¿/\\+=@#$%ˆ&*(){}|~<>;:[\]]{2,}$  -Regex for a name supports multiple langauge


# if __name__ == "__main__":
#     i = 5
#     assert i < 2, "No, i is greater than 2"