###--- CODE ---###
class Stack:
    def __init__(self):
        # TODO: Initialize the Stack
        self.items = list()

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
if __name__ == "__main__":
    stack = Stack()

    stack.push("Web Page 1")
    stack.push("Web Page 2")
    stack.push("Web Page 3")

    print(stack.items)
