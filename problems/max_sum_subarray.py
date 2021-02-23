def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    current_sum = arr[0]  # `current_sum` denotes the sum of a subarray
    # `max_sum` denotes the maximum value of `current_sum` ever
    max_sum = arr[0]

    # Loop from VALUE at index position 1 till the end of the array
    for element in arr[1:]:
        current_sum = max(current_sum + element, element)

        # Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
        max_sum = max(current_sum, max_sum)

    return max_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test case 1
arr = [1, 2, 3, -4, 6]
solution = 8  # sum of array

test_case = [arr, solution]
test_function(test_case)

# test case 2
arr = [1, 2, -5, -4, 1, 6]
solution = 7   # sum of last two elements

test_case = [arr, solution]
test_function(test_case)

# test case 3
arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]

test_case = [arr, solution]
test_function(test_case)
