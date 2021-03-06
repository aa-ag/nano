# Helper Code
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

# --- reversing linkedlist


def reverse(linked_list):
    """
    Reverse the inputted linked list
    """
    reversed_list = LinkedList()
    previous_node = None

    for i in linked_list:
        new_node = Node(i)

        new_node.next = previous_node
        previous_node = new_node

    reversed_list.head = previous_node

    return reversed_list


# testing
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)

# [4, 2, 5, 1, -3, 0]
flipped = reverse(llist)
is_correct = list(flipped) == list(
    [0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
