def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        answer = list()
        for i, character in enumerate(s):
            answer += [character + p for p in permutations(s[:i]+s[i+1:])]
        return answer


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(s)

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


# TESTS
s = 'ab'
solution = ['ab', 'ba']
test_case = [s, solution]
test_function(test_case)


s = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [s, output]
test_function(test_case)


s = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab',
          'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [s, output]
test_function(test_case)
