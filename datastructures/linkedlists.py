# to implement a Linked List
# first, create a "Node" class
# since a Linked List is a list of linked nodes

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
# print(head.value)
# print(head.next)

new_node = Node(2)
head.next = new_node
# then either:
print(new_node.value)
# or
print(head.next.value)
