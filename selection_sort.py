def find_smallest(arr):
    """Находит наименьшее значение списка."""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """Вставляет наименьшие значения в новый список."""
    new_arr = []
    for i in range(len(arr)):
        smallest = int(find_smallest(arr))
        new_arr.append(arr.pop(smallest))
    print(new_arr)


arr = [1, 8, 2, -1, 48]
selection_sort(arr)
