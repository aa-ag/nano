def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """

    # TODO: Write your recursive palindrome checker here
    pass


# Test Cases

print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")
