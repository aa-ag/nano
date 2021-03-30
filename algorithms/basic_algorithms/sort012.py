'''
### Problem Statement

Write a function that takes an input array
(or Python list) consisting of only `0`s, `1`s, and `2`s, 
and sorts that array in a single traversal.

Note that if you can get the function 
to put the `0`s and `2`s in the correct positions, 
this will aotumatically cause the `1`s 
to be in the correct positions as well.
'''


def sort_012(input_list):
    zeros = list()
    ones = list()
    twos = list()

    for i in input_list:
        if i == 0:
            zeros.append(i)
        elif i == 1:
            ones.append(i)
        elif i == 2:
            twos.append(i)

    answer = zeros + ones + twos
    return answer


# tests
def test_function(test_case):
    sort_012(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# test 1
test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

# test 2
test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0,
             2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

# test 3
test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)
