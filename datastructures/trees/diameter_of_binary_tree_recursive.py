# function annotations: ->
# https://www.python.org/dev/peps/pep-3107/
# https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions
from queue import Queue


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert_arr_to_binary_tree(arr):
    """
     Takes arr representing level-order traversal of Binary Tree 
    """
    index = 0
    length = len(arr)

    if length <= 0 or arr[0] == -1:
        return None

    root = Node(arr[index])
    index += 1
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        current_node = queue.get()
        left_child = arr[index]
        index += 1

        if left_child is not None:
            left_node = Node(left_child)
            current_node.left = left_node
            queue.put(left_node)

        right_child = arr[index]
        index += 1

        if right_child is not None:
            right_node = Node(right_child)
            current_node.right = right_node
            queue.put(right_node)
    return root


def max_depths(root):

    if root is None:
        return 0

    return max(max_depths(root.left), max_depths(root.right)) + 1


# tests
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    root = convert_arr_to_binary_tree(arr)
    output = max_depths(root)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test case 1
arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3

test_case = [arr, solution]
test_function(test_case)


# test case 2
arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
solution = 4

test_case = [arr, solution]
test_function(test_case)


# test case 3
arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10,
       None, None, None, None, None, None, 11, None, None, None]
solution = 6

test_case = [arr, solution]
test_function(test_case)
