###--- CREATE STACK ----###
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_stack_empty():
            return None

        temporary_data = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temporary_data

    def stack_top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_stack_empty(self):
        return self.num_elements == 0


###--- USE STACK TO EVALUATE INPUTS ----###
def evaluate_post_fix(input_list):
    stack = Stack()

    for _ in input_list:
        if _.isdigit():
            stack.push(_)

    node = stack.head
    while node:
        print(node.data)
        node = node.next


evaluate_post_fix(["3", "1", "+", "4", "*"])
