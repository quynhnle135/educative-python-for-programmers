class Stack():
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def get_stack(self):
        return self.items


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.get_stack())
print(my_stack.peek())
print(my_stack.is_empty())
my_stack.pop()
print(my_stack.get_stack())