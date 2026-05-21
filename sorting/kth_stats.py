import random

def partition(arr, l, r):
    # выбираем случайный индекс для избегания худшего случая
    pivot_idx = random.randrange(l, r)
    arr[pivot_idx], arr[r - 1] = arr[r - 1], arr[pivot_idx]

    pivot = arr[r - 1]
    i = l
    for j in range(l, r - 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return i

def kth_stats(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None
    
    k -= 1 # 0-индексация
    l, r = 0, len(arr)
    while l < r:
        m = partition(arr, l, r)
        if k == m:
            return arr[m]
        elif k < m:
            r = m
        else:
            l = m + 1
    return arr[l]

print(kth_stats([1, 7, 2, 3, 5], 4)) # 5
print(kth_stats([1, 1, 3, 9, 10], 2)) # 1
print(kth_stats([7, 10, 4, 3, 20, 15], 3)) # 7