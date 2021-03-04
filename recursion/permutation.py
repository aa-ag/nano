import copy


def permute(inputList):
    if inputList == []:
        print([[]])
    elif len(inputList) == 1:
        print([inputList])
    else:
        output = list()

        for i in range(len(inputList), 0, -1):
            output.append(inputList[i-1])

        print([inputList, output])


permute([])  # [[]]
permute([0])  # [[0]]
permute([0, 1])  # [[0, 1], [1, 0]]


# Test Cases

# Helper Function
# def check_output(output, expected_output):
#     o = copy.deepcopy(output)  # so that we don't mutate input
#     e = copy.deepcopy(expected_output)  # so that we don't mutate input

#     o.sort()
#     e.sort()
#     return o == e


# print("Pass" if (check_output(permute([]), [[]])) else "Fail")
# print("Pass" if (check_output(permute([0]), [[0]])) else "Fail")
# print("Pass" if (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
# print("Pass" if (check_output(permute([0, 1, 2]), [[0, 1, 2], [
#       0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")
