items = [8, 3, 1, 7, 0, 10, 2]

pivot_index = len(items) - 1
pivot_value = items[pivot_index]

left_index = 0

while (pivot_index != left_index):

    item = items[left_index]

    if item <= pivot_value:
        left_index += 1
        continue

    # Place the item before the pivot at left_index
    items[left_index] = items[pivot_index - 1]
    # Shift pivot one to the left
    items[pivot_index - 1] = pivot_value
    # Place item at pivot's previous location
    items[pivot_index] = item
    # Update pivot_index
    pivot_index -= 1

print(items)
# [0, 1, 2, 7, 3, 10, 8]
