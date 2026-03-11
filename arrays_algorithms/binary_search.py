def binary_search(arr, target):
    if len(arr) == 0:
        return None
    
    left = 0 # первый элемент в подмассиве
    right = len(arr) - 1 # последний элемент в подмассиве
    middle = (right + left) // 2 # серединный элемент в подмассиве

    while left <= right:  
        if arr[middle] < target:
            left = middle + 1 # отрезаем всё слева, включая middle
        elif arr[middle] > target:
            right = middle - 1 # отрезаем всё справа, включая middle
        else: # arr[middle] == target
            return middle
        
        middle = (right + left) // 2 # обновляем середину
        
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], target=7)) # 3
print(binary_search([1, 5, 6, 7, 9, 10, 13, 16, 18], target=5)) # 1
print(binary_search([1, 2, 3, 4, 5, 6, 7, 9, 10], target=8)) # -1
print(binary_search([1, 2, 3, 3, 8, 9, 10, 11, 11, 12, 13, 18], target=11)) # 7 или 8