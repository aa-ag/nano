class Stack:
    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push_to_stack(self, data):
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1


stack = Stack()
print(stack.arr)
# [None, None, None, None, None, None, None, None, None, None]

stack.push_to_stack(1)
stack.push_to_stack(2)
stack.push_to_stack(3)
print(stack.arr)
# [1, 2, 3, None, None, None, None, None, None, None]
