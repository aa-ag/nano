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

    def push_to_stack(self, value):
        new_node = Node(value)
        # check if stack is empty first
        if self.head is None:
            self.head = new_node
        else:
            # place new node at linked-list's head/top
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def get_stack_size(self):
        return self.num_elements

    def is_stack_empty(self):
        return self.num_elements == 0

    def pop_from_stack(self):
        if self.is_stack_empty():
            return None

        # copy data to a local variable
        value = self.head.value
        # move head pointer to point to next node
        self.head = self.head.next
        self.num_elements -= 1
        return value


###--- TESTS ---###
# Setup
stack = Stack()
stack.push_to_stack(10)
stack.push_to_stack(20)
stack.push_to_stack(30)
stack.push_to_stack(40)
stack.push_to_stack(50)

# Test size
print("Pass" if (stack.get_stack_size() == 5) else "Fail")
