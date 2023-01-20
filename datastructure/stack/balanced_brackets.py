from datastructure.stack.my_stack import Stack


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    for bracket in paren_string:
        if bracket in "([{":
            s.push(bracket)
        else:
            if s.is_empty():
                return False
            else:
                if is_match(bracket, s.peek()):
                    s.pop()
                else:
                    return False

    return True


def is_match(close, open):
    if open == "[" and close == "]":
        return True
    elif open == "(" and close == ")":
        return True
    elif open == "{" and close == "}":
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
