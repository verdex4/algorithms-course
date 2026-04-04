def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        # находим индекс минимального элемента в окне [i+1, len(arr)]
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # текущий элемент делаем минимальным
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([5, 2, 9, 1, 5])) # [1, 2, 5, 5, 9]
print(selection_sort([64, 25, 12, 22, 11])) # [11, 12, 22, 25, 64]