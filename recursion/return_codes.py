def all_codes(number):
    pass


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = all_codes(number)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)


number = 145
solution = ['ade', 'ne']
test_case = [number, solution]
test_function(test_case)


number = 1145
solution = ['aade', 'ane', 'kde']
test_case = [number, solution]
test_function(test_case)


number = 4545
solution = ['dede']
test_case = [number, solution]
test_function(test_case)
