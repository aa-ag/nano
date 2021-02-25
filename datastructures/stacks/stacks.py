###--- CLASS & Methods ---###
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

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

    def handle_stack_capacity(self):
        old_arr = self.arr

        self.arr = [None for _ in range(2 * len(self.arr))]
        for i, element in enumerate(old_arr):
            self.arr[i] = element


###--- DRIVER CODE ---###
if __name__ == "__main__":
    stack = Stack()
    # We first have to push an item so that we'll have something to pop
    stack.push_to_stack("Test")
    print(stack.pop())  # Should return the popped item, which is "Test"
    # Should return None, since there's nothing left in the stack
    print(stack.pop())
