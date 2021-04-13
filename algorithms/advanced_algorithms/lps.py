def lps(input_string):
    '''
     In the solution, we are looping over the elements of our `input_string` 
     using two `for` loops; these are each of $O(N)$ and nested this becomes $O(N^2)$. 
     This behavior dominates our optimized solution.
    '''

    # TODO: Complete this implementation of the LPS function
    # The function should return one value: the LPS length for the given input string
    pass


# TESTS
def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'BxAoNxAoNxA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)

string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)
