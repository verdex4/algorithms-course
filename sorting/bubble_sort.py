def bubble_sort(arr):
    for i in range(len(arr) - 1):
        # заставляем всплыть максимум окна [0, len(arr) - 1 - i] в конец
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([5, 2, 9, 1, 5])) # [1, 2, 5, 5, 9]
print(bubble_sort([2, 1, 3, 4, 8, 6, 11])) # [1, 2, 3, 4, 6, 8, 11]