###--- CREATE LINKED LIST ---###
class Node:
    def __init__(self, data):
        self.data = data
        self.head = None


###--- CREATE QUEUE ---###
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.head
        self.num_elements += 1

###--- TEST ---###
