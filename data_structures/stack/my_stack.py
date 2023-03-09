class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)

print("Peek: ", my_stack.peek())
print("Is my stack empty? ", my_stack.is_empty())
print("My stack: ", my_stack.get_stack())

my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()

print("Is my stack empty? ", my_stack.is_empty())