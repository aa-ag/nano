# Code

def reverse_string(input):
    """
     reverse_string("abc") returns "cba"
    """

    # TODO: Write your recursive string reverser solution here
    if len(input) == 0:
        return ""
    else:
        first_character = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]

        reversed_substring = reverse_string(sub_string)

        return reversed_substring + first_character


# Test Cases
print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
