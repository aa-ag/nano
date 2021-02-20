# Linked List Practice
'''
Implement a linked list class. You have to define a few functions that perform the desirbale action. Your `LinkedList` class should be able to:

+ Append data to the tail of the list and prepend to the head
+ Search the linked list for a value and return the node
+ Remove a node
+ Pop, which means to return the first node's value and delete the node from the list
+ Insert data at some position in the list
+ Return the size (length) of the linked list
'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def to_list(self):
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out


def prepend(self, value):
    """ Prepend a value to the beginning of the list. """
    # TODO: Write function to prepend here
    if self.head == None:
        self.head = Node(value)
        return
    else:
        previous_head = self.head
        self.head = Node(value)
        self.head.next = previous_head
    return


LinkedList.prepend = prepend

# Test prepend
# linked_list = LinkedList()
# linked_list.prepend(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"


def append(self, value):
    """ Append a value to the end of the list. """
    # TODO: Write function to append here
    if self.head is None:
        self.head = Node(value)
        return

    # Move to the tail (the last node)
    node = self.head
    while node.next:
        node = node.next

    node.next = Node(value)
    return


LinkedList.append = append

# Test append - 1
# linked_list.append(3)
# linked_list.prepend(2)
# assert linked_list.to_list() == [
#     2, 1, 3], f"list contents: {linked_list.to_list()}"

# Test append - 2
# linked_list = LinkedList()
# linked_list.append(1)
# assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
# linked_list.append(3)
# assert linked_list.to_list() == [
#     1, 3], f"list contents: {linked_list.to_list()}"


def search(self, value):
    """ Search the linked list for a node with the requested value and return the node. """
    # TODO: Write function to search here
    node = self.head  # start from the head node
    while node != None:
        if node.value == value:
            print(node.value)
            node = node.next


LinkedList.search = search

linked_list = LinkedList()

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(
    1).value == 1, f"list contents: {linked_list.to_list()}"
assert linked_list.search(
    4).value == 4, f"list contents: {linked_list.to_list()}"
