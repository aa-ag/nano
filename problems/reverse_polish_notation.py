###--- CREATE STACK ----###
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_stack_empty():
            return None

        temporary_data = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temporary_data

    def stack_top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_stack_empty(self):
        return self.num_elements == 0


###--- USE STACK TO EVALUATE INPUTS ----###
def evaluate_post_fix(input_list):
    stack = Stack()

    for element in input_list:
        if element == '*':
            second_num_in_pair = stack.pop()
            first_num_in_pair = stack.pop()
            operation_result = first_num_in_pair * second_num_in_pair
            stack.push(operation_result)
        elif element == '/':
            second_num_in_pair = stack.pop()
            first_num_in_pair = stack.pop()
            operation_result = int(first_num_in_pair / second_num_in_pair)
            stack.push(operation_result)
        elif element == '+':
            second_num_in_pair = stack.pop()
            first_num_in_pair = stack.pop()
            operation_result = first_num_in_pair + second_num_in_pair
            stack.push(operation_result)
        elif element == '-':
            second_num_in_pair = stack.pop()
            first_num_in_pair = stack.pop()
            operation_result = first_num_in_pair - second_num_in_pair
            stack.push(operation_result)
        else:
            stack.push(int(element))

    return stack.pop()  # pop for top element


###--- TESTS ---###
def test_function(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function(test_case_1)


test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function(test_case_2)


test_case_3 = [["10", "6", "9", "3", "+", "-11",
                "*", "/", "*", "17", "+", "5", "+"], 22]
test_function(test_case_3)
