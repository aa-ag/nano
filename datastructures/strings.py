# Exercise 1. Reverse Strings

def string_reverser(our_string):
    '''
     In this first exercise, the goal is to write a function 
     that takes a string as input and then returns the reversed string.
    '''
    return our_string[::-1]


# print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
# print("Pass" if ('!noitalupinam gnirts gnicitcarP' ==
#                  string_reverser('Practicing string manipulation!')) else "Fail")
# print("Pass" if ('3432 :si edoc esuoh ehT' ==
#                  string_reverser('The house code is: 2343')) else "Fail")


# Exercise 2.  Anagrams
def anagram_checker(str1, str2):
    '''
    The goal of this exercise is to write some code 
    to determine if two strings are anagrams of each other.
    An anagram is a word (or phrase) 
    that is formed by rearranging the letters of another word (or phrase).
    '''
    return sorted(str1.replace(' ', '').lower()) == sorted(str2.replace(' ', '').lower())


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man',
                                'Notified madman into water') else "Fail")
