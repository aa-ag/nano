def smallest_positive(l):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_postive_number = None
    for number in l:
        if number > 0:
            if smallest_postive_number == None or number < smallest_postive_number:
                smallest_postive_number = number
    return smallest_postive_number


# Test cases
print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None
