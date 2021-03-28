def sort_a_little_bit(items):
    left_index = 0
    pivot_index = len(items) - 1
    pivot_value = items[pivot_index]

    while (pivot_index != left_index):

        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1


items = [8, 3, 1, 7, 0, 10, 2]
sort_a_little_bit(items)
print(items)
