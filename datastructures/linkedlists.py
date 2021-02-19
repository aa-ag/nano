# to implement a Linked List
# first, create a "Node" class
# since a Linked List is a list of linked nodes

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(2)
print(head.value)
