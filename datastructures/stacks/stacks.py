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

    def handle_stack_capacity(self):
        old_arr = self.arr

        self.arr = [None for _ in range(2 * len(self.arr))]
        for i, element in enumerate(old_arr):
            self.arr[i] = element

    # TODO: Add the size method
    def size(self):
        return len(self.arr)

    # TODO: Add the is_empty method
    def is_empty(self):
        return all(i == None for i in self.arr)


###--- DRIVER CODE ---###
if __name__ == "__main__":
    stack = Stack()
    print(stack.size())  # Should return 0
    print(stack.is_empty())  # Should return True
    # Let's push an item onto the stack and check again
    stack.push_to_stack("Test")
    print(stack.size())  # Should return 1
    print(stack.is_empty())  # Should return False
