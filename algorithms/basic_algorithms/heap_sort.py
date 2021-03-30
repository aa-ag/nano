'''
The main steps in a heapsort are:

Convert the array into a maxheap (a complete binary tree with decreasing values)
Swap the top element with the last element in the array (putting it in it's correct final position)
Repeat with arr[:len(arr)-1] (all but the sorted elements)
'''


def heapsort(arr):
    heapify(arr, len(arr), 0)


def heapify():
    """
    :param: arr - array to heapify
    n -- number of elements in the array
    i -- index of the current node
    TODO: Converts an array (in place) into a maxheap, a complete binary tree with the largest values at the top
    """


def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)
