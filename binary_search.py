def binary_search(list, item):
    """Ищет порядковый номер элемента в заданном списке."""
    low = 0  # Переменная обозначающая индекс начала списка.
    high = len(list) - 1  # Переменная обозначающая конец списка.

    while low <= high:  # Пока есть элементы в списке
        mid = (low + high) // 2  # Индекс элемента в середине списка.
        guess = list[mid]  # Элемент находящийся в середине списка.
        if guess == item:  # Если наша середина равна нужному элементу, выводим индекс.
            return mid
        elif guess > item:  # Если середина больше чем искомый объект, поиск продолжается в меньшей половине списка.
            high = mid - 1
        else:  # Во всех остальных случаях, поиск происходит в большей половине списка.
            low = mid + 1
    return None


def binary_search_recursive(list, item, start_list, end_list):
    if start_list >= end_list:
        return None
    else:
        mid = (start_list + end_list) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            return binary_search_recursive(list, item, start_list, mid)
        else:
            return binary_search_recursive(list, item, mid, start_list)


my_list = [1, 3, 5, 7, 9]

print(binary_search_recursive(my_list, 3, 0, len(my_list)))
print(binary_search_recursive(my_list, -1, 0, len(my_list)))
