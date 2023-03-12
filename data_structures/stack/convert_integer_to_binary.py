from stack_introduction import Stack

def convert_int_to_bin(number):
    if number == 0:
        return 0

    binary_stack = Stack()
    while number > 0:
        remainder = number % 2
        binary_stack.push(remainder)
        number = number // 2
    binary_number = 0
    while not binary_stack.is_empty():
        binary_number = binary_number * 10 + binary_stack.pop()
    return binary_number

print(convert_int_to_bin(242))
print(convert_int_to_bin(56))
print(convert_int_to_bin(2))
print(convert_int_to_bin(32))
print(convert_int_to_bin(10))