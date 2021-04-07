# Your solution
def min_operations():
    """
    Return number of steps taken to reach a target number
    input: target number (as an integer)
    output: number of steps (as an integer)
    """
    pass


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
