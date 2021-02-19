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

# new_node = Node(2)
# head.next = new_node
# alternatively
head.next = Node(2)
# then either:
# print(new_node.value)
# or
# print(head.next.value)

# Step 2.  Add three more nodes to the list, with the values `4`, `3`, and `5`

head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

print(head.value)
print(head.next.value)
print(head.next.next.value)
print(head.next.next.next.value)
print(head.next.next.next.next.value)
