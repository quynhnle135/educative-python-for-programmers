from stack_introduction import Stack

def reverse_string(given_string):
    reversed_stack = Stack()
    reversed_string = ""
    for letter in given_string:
        reversed_stack.push(letter)
    while not reversed_stack.is_empty():
        reversed_string += reversed_stack.pop()
    return reversed_string


my_string = "Hi my name is Quinn"
reversed_string = my_string[::-1]
print(my_string)
print(reversed_string)
print(reverse_string(my_string))

