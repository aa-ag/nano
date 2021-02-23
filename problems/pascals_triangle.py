def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """
    pass


# tests
def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


# test 1
n = 0
solution = [1]

test_case = [n, solution]
test_function(test_case)

# test 2
n = 1
solution = [1, 1]

test_case = [n, solution]
test_function(test_case)

# test 3
n = 2
solution = [1, 2, 1]

test_case = [n, solution]
test_function(test_case)


# test 4
n = 3
solution = [1, 3, 3, 1]

test_case = [n, solution]
test_function(test_case)

# test 5
n = 4
solution = [1, 4, 6, 4, 1]

test_case = [n, solution]
test_function(test_case)
