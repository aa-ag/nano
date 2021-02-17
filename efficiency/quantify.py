######------ 1 ------######

def some_function(n):
    '''
     adds 200 to input n
    '''
    for i in range(2):
        n += 100
    print(n)


# some_function(10)


######------ 2 ------######

def other_function(n):
    for i in range(100):
        n += 2
    print(n)


other_function(10)
