# Solution
def subsets(arr):
    return return_subsets(arr, 0)


def return_subsets(arr, index):
    if index >= len(arr):
        return [[]]

    small_output = return_subsets(arr, index + 1)

    output = list()
    # append existing subsets
    for element in small_output:
        output.append(element)

    # add current elements to existing subsets and add them to the output
    for element in small_output:
        current = list()
        current.append(arr[index])
        current.extend(element)
        output.append(current)
    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = subsets(arr)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# test 1
arr = [9]
solution = [[], [9]]

test_case = [arr, solution]
test_function(test_case)


# test 2
arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)


# test 3
arr = [9, 12, 15]
solution = [[], [15], [12], [12, 15], [9], [9, 15], [9, 12], [9, 12, 15]]

test_case = [arr, solution]
test_function(test_case)


# test 4
arr = [9, 8, 9, 8]
solution = [[],
            [8],
            [9],
            [9, 8],
            [8],
            [8, 8],
            [8, 9],
            [8, 9, 8],
            [9],
            [9, 8],
            [9, 9],
            [9, 9, 8],
            [9, 8],
            [9, 8, 8],
            [9, 8, 9],
            [9, 8, 9, 8]]

test_case = [arr, solution]
test_function(test_case)
