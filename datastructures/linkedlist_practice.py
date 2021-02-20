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


# Task 1. Write definition of `prepend()` function and test its functionality
# Define a function outside of the class
# https://stackoverflow.com/questions/9455111/define-a-method-outside-of-class-definition
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


# This is the way to add a function to a class after it has been defined
LinkedList.prepend = prepend

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.to_list() == [1], f"list contents: {linked_list.to_list()}"
