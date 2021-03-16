def recursive_binary_search(target, source, left=0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)


def find_first(target, source):
    '''
     sets an index `i`
     if there isn't an index 
     where target is found in source, return None
     alternatively, where there's a match,
     if it's the very first element in source, return 0
     else move left and check
     else, return the index
    '''
    i = recursive_binary_search(target, source)

    if not i:
        return None
    while source[i] == target:
        if i == 0:
            return 0
        if source[i - 1] == target:
            i -= 1
        else:
            return i


multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 3
print(find_first(9, multiple))  # Should return None
