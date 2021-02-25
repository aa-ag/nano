class Stack:
    def __init__(self, initial_size=10):
        self.arr = [None for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push_to_stack(self, data):
        if self.next_index == len(self.arr):
            print("Stackoverflow! Increasing capacity...")
            self.handle_stack_capacity()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def handle_stack_capacity(self):
        old_arr = self.arr

        self.arr = [None for _ in range(2 * len(self.arr))]
        for i, element in enumerate(old_arr):
            self.arr[i] = element


stack = Stack()
print(stack.arr)
# [None, None, None, None, None, None, None, None, None, None]

for _ in range(11):
    stack.push_to_stack(_)

print(stack.arr)
# [1, 2, 3, None, None, None, None, None, None, None]
