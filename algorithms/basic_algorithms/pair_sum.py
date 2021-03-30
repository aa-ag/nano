def pair_sum(a, t):
    # sort the list
    a.sort()

    # initialize two pointer - one from start of the array and other from the end
    front_index = 0
    back_index = len(a) - 1

    # shift the pointers
    while front_index < back_index:
        front = a[front_index]
        back = a[back_index]

        if front + back == target:
            return [front, back]
        elif front + back < target:       # sum < target ==> shift front pointer forward
            front_index += 1
        else:
            back_index -= 1               # sum > target ==> shift back pointer backward

    return [None, None]


# tests
def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


# test 1
input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)


# test 2
input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)


# test 3
input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
