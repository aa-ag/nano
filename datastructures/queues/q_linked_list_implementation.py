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

    def dequeue(self, data):
        if self.is_empty():
            return None
        old_head = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return old_head

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


###--- TEST ---###
