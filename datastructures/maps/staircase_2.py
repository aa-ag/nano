def staircase(n):
    if n <= 0:
        return 1
    elif n == 1 or n == 2:
        return n
    elif n == 3:
        return 4

    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


# Tests
def test_function(test_case):
    answer = staircase(test_case[0])
    if answer == test_case[1]:
        print("Pass")
    else:
        print("Fail")


# test 1
test_case = [4, 7]
test_function(test_case)


# test 2
test_case = [5, 13]
test_function(test_case)


# test 3
test_case = [3, 4]
test_function(test_case)


# test 4
test_case = [20, 121415]
test_function(test_case)
