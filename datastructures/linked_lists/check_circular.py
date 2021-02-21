###--- CHECK IF LINKEDLIST IS CIRCULAR ---###

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, init_list=None):
        self.head = None
        if init_list:
            for value in init_list:
                self.append(value)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
        return


list_with_loop = LinkedList([2, -1, 3, 0, 5])

# Creating a loop where the last node points back to the second node
loop_start = list_with_loop.head.next

node = list_with_loop.head
while node.next:
    node = node.next
node.next = loop_start


def iscircular(linked_list):
    """
     Determine whether the Linked List is circular or not
    """

    # TODO: Write function to check if linked list is circular

    slow_runner = linked_list.head
    fast_runner = linked_list.head

    while True:
        try:
            slow_runner = slow_runner.next
            fast_runner = fast_runner.next.next
            if slow_runner.value == fast_runner.value:
                return True
            elif slow_runner is fast_runner:
                return False
        except:
            return False


# Test Cases
# Create another circular linked list
small_loop = LinkedList([0])
small_loop.head.next = small_loop.head

print("Pass 1/5" if iscircular(list_with_loop) else "Fail 1/5")
# Pass
print("Pass 2/5" if iscircular(LinkedList([-4, 7, 2, 5, -1])) else "Fail 2/5")
# Fail
print("Pass 3/5" if iscircular(LinkedList([1])) else "Fail 3/5")
# Fail
print("Pass 4/5" if iscircular(small_loop) else "Fail 4/5")
# Pass
print("Pass 5/5" if iscircular(LinkedList([])) else "Fail 5/5")
# Fail
