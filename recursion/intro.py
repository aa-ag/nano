# def power_of_2(n):
#     if n == 0:
#         return 1

#     return 2 * power_of_2(n - 1)


# print(power_of_2(2))
# print(power_of_2(5))

'''
 Implement `sum_integers(n)` to  calculate the sum of all integers 
 from 1 to n using recursion. For example, `sum_integers(3)` 
 should return 6 (1 + 2 + 3).
'''


def sum_integers(n):
    if n == 1:
        return 1
    return n + sum_integers(n - 1)


print(sum_integers(3))
