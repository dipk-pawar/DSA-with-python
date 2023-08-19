my_list = [10, 9, 8, 4, 5, 6, 7, 1, 3, 2]
new_list = []

# Outer loop: Iterate (len(my_list) - 1) times
for _ in range(len(my_list) - 1):
    # Inner loop: Iterate (len(my_list) - 1) times
    for i in range(len(my_list) - 1):
        # Compare adjacent elements
        if my_list[i] > my_list[i+1]:
            # Swap the elements if they are in the wrong order
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

# Output the sorted list
print(my_list)
