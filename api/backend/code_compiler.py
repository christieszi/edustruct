import re

def evaluate_code(code):
    try:
        exec(code)
    except Exception as e:
        print("error in code")
        return e
    return None


def compile_block(block):
    code = get_code_from_block(block)
    return evaluate_code(code)

def get_code_from_block(block):
    # need to get the line of code from the block
    code = block['code'] # placeholder for now
    return format_code(code)


def format_code(code):
    # Regular expression to match simple control structures
    pattern = r'(if|elif|else|for|while)\s+.*?:\s*(.*)'
    formatted_code = re.sub(pattern, r'\1:\n    \2', code)
    return formatted_code

inputgiven = "print('Hello World')"

if __name__ == "__main__":
    evaluate_code(inputgiven)
    
