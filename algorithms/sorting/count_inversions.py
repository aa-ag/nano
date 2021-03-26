def count_inversions(arr):
    # TODO: Complete this function
    pass


# testing
def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


# test 1
arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

# test 2
arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

# test 3
arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)
