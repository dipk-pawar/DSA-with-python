def merge_sort(sorting_list):

    if len(sorting_list) <= 1:
        return
    mid_value = len(sorting_list) // 2
    left_list = sorting_list[:mid_value]
    right_list = sorting_list[mid_value:]
    merge_sort(left_list)
    merge_sort(right_list)
    i = 0
    j = 0
    k = 0

    while len(left_list) > i and len(right_list) > j:
        if left_list[i] < right_list[j]:
            sorting_list[k] = left_list[i]
            i += 1
        else:
            sorting_list[k] = right_list[j]
            j += 1
        k = k + 1
    while len(left_list) > i:
        sorting_list[k] = left_list[i]
        i += 1
        k = k + 1

    while len(right_list) > j:
        sorting_list[k] = right_list[j]
        j += 1
        k = k + 1


my_list = [8, 6, 5, 7, 9, 4, 2, 3, 1, 5]

merge_sort(my_list)

print(my_list)