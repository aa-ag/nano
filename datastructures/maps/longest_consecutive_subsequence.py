def longest_consecutive_subsequence(input_list):
    '''
     return the sorted longest (sub) list of consecutive numbers present anywhere in the given list.
     For example, given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5
    '''
    pass


# Tests
def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


# test 1
test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)


# test 2
test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20,
                25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)


# test 3
test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)
