def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        # integer division in Python 3
        mid_index = (start_index + end_index)//2

        mid_element = array[mid_index]

        # we have found the element
        if target == mid_element:
            return mid_index

        # the target is less than mid element
        # we will only search in the left half
        elif target < mid_element:
            end_index = mid_index - 1

        # the target is greater than mid element
        else:
            # we will search only in the right half
            start_index = mid_element + 1

    return -1


# test
def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
index = 11
test_case = [array, target, index]
test_function(test_case)
