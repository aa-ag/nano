###--- CODE ---###
class Stack:
    def __init__(self):
        # TODO: Initialize the Stack
        self.items = []

    def size(self):
        # TODO: Check the size of the Stack
        return len(self.items)

    def push(self, item):
        # TODO: Push item onto Stack
        return self.items.append(item)

    def pop(self):
        # TODO: Pop item off of the Stack
        return self.items.pop()


###--- DRIVER CODE ---###

stack = Stack()

stack.push("Web Page 1")
stack.push("Web Page 2")
stack.push("Web Page 3")

print(stack.items)

stack.pop()
stack.pop()

print("Pass" if (stack.items[0] == 'Web Page 1') else "Fail")
