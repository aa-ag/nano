######------ 1 ------######

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
# print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

# print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

# print(smallest_positive([-6, -9, -7]))
# Correct output: None

# print(smallest_positive([]))
# Correct output: None


######------ 2 ------######

# This exercise uses a data structure that stores Udacity course information.
# The data structure format is:

#    { <semester>: { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }


courses = {
    'spring2020': {'cs101': {'name': 'Building a Search Engine',
                             'teacher': 'Dave',
                             'assistant': 'Peter C.'},
                   'cs373': {'name': 'Programming a Robotic Car',
                             'teacher': 'Sebastian',
                             'assistant': 'Andy'}},
    'fall2020': {'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': {'cs001': {'name': 'Building a Quantum Holodeck',
                             'teacher': 'Dorina'},
                   'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                             'teacher': 'Jasper'},
                   }
}


def when_offered(courses, course):
    # TODO: Fill out the function here.

    # TODO: Return list of semesters here.
    return [k for k, v in courses.items() if course in v]


print(when_offered(courses, 'cs101'))
# Correct result:
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result:
# []
