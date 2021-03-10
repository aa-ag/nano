def staircase(n):
    # Base Case - What holds true for minimum steps possible
    # i.e., n == 1? Return the number of ways the child can
    # climb one step.

    # Inductive Hypothesis - What holds true for n == 2 or n == 3?
    # Return the number of ways to climb them.

    # Inductive Step (n > 3) - use Inductive Hypothesis
    # to formulate a solution

    pass


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
