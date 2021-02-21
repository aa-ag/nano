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


def print_all_nodes(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


# print_all_nodes(head)

# Creating a Linked List, less manual

# O(n^2)
# def create_linked_list(input_list):
#     head = None
#     for value in input_list:
#         if head is None:
#             head = Node(value)
#         else:
#             # Move to the tail (the last node)
#             current_node = head
#             while current_node.next:
#                 current_node = current_node.next

#             current_node.next = Node(value)
#     return head

# O(n)
def create_linked_list_better(input_list):

    head = None
    tail = None

    for value in input_list:

        if head is None:
            head = Node(value)
            tail = head
        else:
            tail.next = Node(value)
            tail = tail.next        # update the tail

    return head


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = [1]
head = create_linked_list_better(input_list)
test_function(input_list, head)

input_list = []
head = create_linked_list_better(input_list)
test_function(input_list, head)
