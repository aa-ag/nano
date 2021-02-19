# implement a Linked List

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

# Exercise 2 -  Traversing the list

current_node = head

while current_node is not None:
    print(current_node.value)
    current_node = current_node.next
