from printing_problems import *

def evaluate_code(code):
    try:
        exec(code)
    except Exception as e:
        print("error in code")
        return e
    return None

# get the string of the block the user has chosen
def get_block_string():
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
            code += get_block_string()
            l += len(get_block_string())
            r += len(get_block_string())
    return code


# if __name__ == "__main__":
#     i = 5
#     assert i < 2, "No, i is greater than 2"