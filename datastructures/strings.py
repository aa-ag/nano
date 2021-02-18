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
# def anagram_checker(str1, str2):
#     '''
#     The goal of this exercise is to write some code
#     to determine if two strings are anagrams of each other.
#     An anagram is a word (or phrase)
#     that is formed by rearranging the letters of another word (or phrase).
#     '''
#     return sorted(str1.replace(' ', '').lower()) == sorted(str2.replace(' ', '').lower())


# print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
# print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
# print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
# print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
# print("Pass" if anagram_checker('Time and tide wait for no man',
#                                 'Notified madman into water') else "Fail")


# Exercise 3.  Reverse the words in sentence

# def word_flipper(our_string):
#     '''
#     Given a sentence, reverse each word in the sentence
#     while keeping the order the same
#     '''
#     return ' '.join([i[::-1] for i in our_string.split()])


# print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
# print("Pass" if ('sihT si na elpmaxe' ==
#                  word_flipper('This is an example')) else "Fail")
# print("Pass" if ('sihT si eno llams pets rof ...' ==
#                  word_flipper('This is one small step for ...')) else "Fail")


# Exercise 4.  Hamming Distance

def hamming_distance(str1, str2):
    '''
     In information theory, 
     the Hamming distance between two strings of equal length
     is the number of positions at which the corresponding symbols are different.
    '''
    if len(str1) != len(str2):
        return None
    else:
        positions_at_which_the_corresponding_symbols_are_different = 0

        for i in range(len(str1)):
            if str1[i] != str2[i]:
                positions_at_which_the_corresponding_symbols_are_different += 1
        return positions_at_which_the_corresponding_symbols_are_different


# Test Cases
print("Pass" if (10 == hamming_distance('ACTTGACCGGG', 'GATCCGGTACA')) else "Fail")
print("Pass" if (1 == hamming_distance('shove', 'stove')) else "Fail")
print("Pass" if (None == hamming_distance(
    'Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if (2 == hamming_distance(
    '0101010100011101', '0101010100010001')) else "Fail")
