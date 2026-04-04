def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparisons, swaps

def selection_sort(arr):
    comparisons = 0
    swaps = 0
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        swaps += 1
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparisons, swaps

sorted_arr, comp, swaps = bubble_sort([2, 3, 1, 7, 9, 11, 34, 22, 20, 4])
print(f"Сортировка пузырьком: {sorted_arr}, сравнений: {comp}, обменов: {swaps}")
sorted_arr, comp, swaps = selection_sort([2, 3, 1, 7, 9, 11, 34, 22, 20, 4])
print(f"Сортировка выбором: {sorted_arr}, сравнений: {comp}, обменов: {swaps}")