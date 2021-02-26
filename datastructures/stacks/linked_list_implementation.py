# implementing a stack
# using a linked list


# first, creating a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None  # No items in stack yet, so head is None
        self.num_elements = 0  # No items in stack yet, so num_elements is 0
