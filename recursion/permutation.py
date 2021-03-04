import copy                                           # `copy` module

# first, understand id()
foo = 257
bar = foo
baz = bar
fii = 257

print(id(foo))
print(id(bar))
print(id(baz))
print(id(fii))


# list1 = [0, 1, 2]
# list2 = [7, 8, 9]
# # create a compound object
# compoundList1 = [list1, list2]


# '''ASSIGNMENT OPERATION - Points a new reference to the existing object.'''
# compoundList2 = compoundList1

# # id() - returns the identity of the object passed
# # True - compoundList2 is the same object as compoundList1
# print(id(compoundList1) == id(compoundList2))
# # True - compoundList2[0] is the same object as compoundList1[0]
# print(id(compoundList1[0]) == id(compoundList2[0]))


# '''SHALLOW COPY'''
# compoundList2 = copy.copy(compoundList1)

# # False - compoundList2 is now a new object
# print(id(compoundList1) == id(compoundList2))
# # True - compoundList2[0] is the same object as compoundList1[0]
# print(id(compoundList1[0]) == id(compoundList2[0]))


# '''DEEP COPY'''
# compoundList2 = copy.deepcopy(compoundList1)

# # False - compoundList2 is now a new object
# print(id(compoundList1) == id(compoundList2))
# # False - compoundList2[0] is now a new object
# print(id(compoundList1[0]) == id(compoundList2[0]))
