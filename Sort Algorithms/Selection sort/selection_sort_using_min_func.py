my_list = [3, 9, 5, 2, 7, 1, 4, 8, 6]

# Iterate over indices i from 0 to the length of the list minus 1
for i in range(len(my_list)):
    # Find the minimum value in the remaining unsorted portion of the list
    min_value = min(my_list[i:])

    # Find the index of the minimum value in the list, starting from index i
    min_index = my_list.index(min_value, i)

    # If the current element is not the same as the minimum value,
    # swap them to place the minimum value in its correct sorted position
    if my_list[i] != my_list[min_index]:
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

# Output the sorted list
print(my_list)
