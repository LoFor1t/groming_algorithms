def sum_of_list(list):
    sum = 0
    while len(list) > 0:
        sum += list.pop()
    return sum


def sum_of_list_recursive(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_of_list(list[1:])


my_list = [2, 4, 6]

print(sum_of_list(my_list[:]))
print(sum_of_list_recursive(my_list[:]))
