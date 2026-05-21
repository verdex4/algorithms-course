def median(arr, l, r):
    """Ищет медиану трёх."""
    mid = (l + r - 1) // 2
    if arr[l] > arr[mid]:
        arr[l], arr[mid] = arr[mid], arr[l]

    if arr[l] > arr[r-1]:
        arr[l], arr[r-1] = arr[r-1], arr[l]

    if arr[mid] > arr[r-1]:
        arr[mid], arr[r-1] = arr[r-1], arr[mid]

    return arr[mid]

def partition(arr, l, r):
    if r - l < 1:
        return l
    
    i = l
    j = r - 1
    X = median(arr, l, r)

    while i < j:
        while arr[i] < X:
            i += 1
        while arr[j] > X:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break
    
    return i

def quick_sort(arr, l, r):
    if r - l <= 1:
        return arr
    
    m = partition(arr, l, r)
    quick_sort(arr, l, m)
    quick_sort(arr, m, r)
    return arr

print(quick_sort([3, 7, 2, 9, 5], 0, 5)) # [2, 3, 5, 7, 9]
print(quick_sort([7, 2, 1, 6, 8, 5, 3, 4], 0, 8)) # [1, 2, 3, 4, 5, 6, 7, 8]