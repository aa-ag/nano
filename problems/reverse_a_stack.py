###--- CREATE STACK & METHODS ---###
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
        if self.is_empty():
            return None
        temporary_data = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temporary_data

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


###--- REVERSE STACK ---###
def reverse_stack(stack):
    if stack.is_empty():
        return -1
    if stack.size() == 1:
        return stack
    else:
        new_stack = Stack()

        node = stack.head
        while node:
            new_stack.push(stack.pop())
            node = node.next

    return new_stack

###--- TESTS ---###


def test_function(test_case):
    stack = Stack()
    for num in test_case:
        stack.push(num)

    reverse_stack(stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_0 = []
test_function(test_case_0)


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)


test_case_2 = [1]
test_function(test_case_2)
