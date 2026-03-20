def find_max(arr):
    if len(arr) == 0:
        return None
    
    max_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
    return max_value

print(find_max([3, 7, 2, 9, 5])) # 9
print(find_max([-10, -4, -32, -1])) # -1
print(find_max([5, -1, 8, 3, -14, 7])) # 8
print(find_max([])) # None