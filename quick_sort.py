def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        lower = []
        greeter = []
        pivot = array[0]
        for i in array[1:]:
            if i < pivot:
                lower.append(i)
            else:
                greeter.append(i)
        return quick_sort(lower) + [pivot] + quick_sort(greeter)


arr = [8, 1, 5, 6]
print(quick_sort(arr))
