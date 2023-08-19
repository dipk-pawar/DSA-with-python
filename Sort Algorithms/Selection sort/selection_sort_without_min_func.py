my_list = [3, 9, 5, 2, 7, 1, 4, 8, 6]

# Iterate over indices i from 0 to the length of the list minus 1
for i in range(len(my_list)):
    # Inner loop: Iterate over indices j from i + 1 to the end of the list
    for j in range(i + 1, len(my_list)):
        # Compare the element at index j with the element at index i
        if my_list[j] < my_list[i]:
            # Swap the elements if the element at index j is smaller than the element at index i
            my_list[i], my_list[j] = my_list[j], my_list[i]

# Output the sorted list
print(my_list)
