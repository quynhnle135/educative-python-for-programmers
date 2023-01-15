class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def traverse(head_node):
    current_node = head_node
    while current_node:
        print(current_node.value, " -> ", end="")
        current_node = current_node.next
    print("null")


def reverse(head_node):
    prev = None
    current_node = head_node
    while current_node:
        next_node = current_node.next
        current_node.next = prev
        prev = current_node
        current_node = next_node
    return prev


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
traverse(head)
traverse(reverse(head))