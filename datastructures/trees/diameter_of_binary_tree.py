# Note: Diameter of a Binary Tree
# is the maximum distance between
# any two nodes

class BinaryTreeNode:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def diameter_of_binary_tree(root):
    pass


# tests
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    root = convert_arr_to_binary_tree(arr)
    output = diameter_of_binary_tree(root)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3, 4, 5, None, None, None, None, None, None]
solution = 3

test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, 3, 4, None, 5, None, None, None, None, None]
solution = 4

test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, 3, None, None, 4, 5, 6, None, 7, 8, 9, 10,
       None, None, None, None, None, None, 11, None, None, None]
solution = 6

test_case = [arr, solution]
test_function(test_case)
