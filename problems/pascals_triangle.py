# def nth_row_pascal(n):
#     """
#     :param: - n - index (0 based)
#     return - list() representing nth row of Pascal's triangle
#     """
#     # return [int(i) for i in str(11 ** n)]
#     # CLASS CODE
#     if n == 0:
#         return [1]

#     current_row = [1]  # First row

#     ''' Loop from 1 to n; `i` denotes the row number'''
#     for i in range(1, n + 1):
#         # Set the `current_row` from previous iteration as the `previous_row`
#         previous_row = current_row

#         # Let's build the fresh current_row gradually
#         # add the default first element at the 0^th index of the `i^th` row
#         current_row = [1]

#         '''Loop from 1 to (i-1); `j` denotes the index of an element with in the `i^th` row'''
#         # Example, for 5th row we have considered n=4,
#         # we will iterate index from 1 to 3, because
#         # the default element at the 0^th index has already been added
#         for j in range(1, i):

#             # An element at position `j` in the current row is the
#             # sum of elements at position `j` and `j-1` in the previous row.
#             next_number = previous_row[j] + previous_row[j - 1]

#             # Append the new element to the current_row
#             current_row.append(next_number)

#         current_row.append(1)  # append the default last element
#     return current_row


# # tests
# def test_function(test_case):
#     n = test_case[0]
#     solution = test_case[1]
#     output = nth_row_pascal(n)
#     if solution == output:
#         print("Pass")
#     else:
#         print("Fail")


# # test 1
# n = 0
# solution = [1]

# test_case = [n, solution]
# test_function(test_case)

# # test 2
# n = 1
# solution = [1, 1]

# test_case = [n, solution]
# test_function(test_case)

# # test 3
# n = 2
# solution = [1, 2, 1]

# test_case = [n, solution]
# test_function(test_case)


# # test 4
# n = 3
# solution = [1, 3, 3, 1]

# test_case = [n, solution]
# test_function(test_case)

# # test 5
# n = 4
# solution = [1, 4, 6, 4, 1]

# test_case = [n, solution]
# test_function(test_case)


# print actual pascal triangle

def print_pascal_triangle(n):
    '''
     Time Complexity: O(N).
     Each row is an incrementing power of 11 from 0 to n
    '''
    for i in range(n):
        # format/adjust space
        print(' '*(n-i), end='')

        # compute power of 11, each digit separated by a space
        print(' '.join(map(str, str(11**i))))


# --- DRIVER CODE ---
if __name__ == "__main__":
    print_pascal_triangle(10)

'''
          1
         1 1
        1 2 1
       1 3 3 1
      1 4 6 4 1
     1 6 1 0 5 1
    1 7 7 1 5 6 1
   1 9 4 8 7 1 7 1
  2 1 4 3 5 8 8 8 1
 2 3 5 7 9 4 7 6 9 1
'''
