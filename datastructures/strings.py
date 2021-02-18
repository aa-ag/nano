# Exercise 1. Reverse Strings

'''
 In this first exercise, the goal is to write a function 
 that takes a string as input and then returns the reversed string.
'''


def string_reverser(our_string):
    return our_string[::-1]


print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==
                 string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' ==
                 string_reverser('The house code is: 2343')) else "Fail")
