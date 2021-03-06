# def add(num_one, num_two):
#     output = num_one + num_two
#     custom_print(output, num_one, num_two)
#     return output


# def custom_print(output, num_one, num_two):
#     print("The sum of {} and {} is: {}".format(num_one, num_two, output))


# result = add(5, 7)

def print_integers(n):
    if n <= 0:
        return
    print(n)
    print_integers(n - 1)


print_integers(5)
