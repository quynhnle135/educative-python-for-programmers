from stack_introduction import Stack

def is_matched(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def determine_balanced_brackets(parentheses):
    open_paren = Stack()
    is_balanced = True
    index = 0

    while index < len(parentheses) and is_balanced:
        paren = parentheses[index]
        if paren in "{([":
            open_paren.push(paren)
        else:
            if open_paren.is_empty():
                is_balanced = False
                break
            else:
                top = open_paren.pop()
                if not is_matched(top, paren):
                    is_balanced = False
                    break
        index += 1

    if open_paren.is_empty() and is_balanced:
        return True
    else:
        return False

print("String : (((({})))) Balanced or not?")
print(determine_balanced_brackets("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(determine_balanced_brackets("[][]]]"))

print("String : [][] Balanced or not?")
print(determine_balanced_brackets("[][]"))





