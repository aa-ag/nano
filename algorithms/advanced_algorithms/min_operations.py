# Your solution
def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    temporary = 0
    count = 0
    while temporary < target:
        pass
        # if a certain type
        # then + 1
        # else * 2
        # and also count + 1
    # return count


# Test Cases
def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = min_operations(target)

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test 1
target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)


# test 2
target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)
