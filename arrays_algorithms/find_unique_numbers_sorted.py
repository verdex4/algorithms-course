def find_unique_numbers_sorted(arr):
    if len(arr) == 0:
        return None
    
    prev_num = arr[0]
    unique_numbers = [prev_num]

    for i in range(1, len(arr)):
        if arr[i] != prev_num:
            prev_num = arr[i]
            unique_numbers.append(arr[i])
            
    return unique_numbers

print(find_unique_numbers_sorted([1, 1, 2, 2, 2, 3, 4, 4, 5])) # [1, 2, 3, 4, 5]
print(find_unique_numbers_sorted([3, 5, 7, 7, 9, 10, 10])) # [3, 5, 7, 9, 10]
print(find_unique_numbers_sorted([])) # None