def find_unique_numbers(arr):
    if len(arr) == 0:
        return None
    
    unique_numbers = []
    seen = [] # уже встреченные числа
    for num in arr:
        is_unique = True # предполагаем, что число уникальное
        for seen_num in seen:
            if num == seen_num:
                # увидели в уже попадавшихся числах -> не уникальное
                is_unique = False
                break
        if is_unique:
            unique_numbers.append(num)
            seen.append(num)
    
    return unique_numbers

print(find_unique_numbers([1, 3, 2, 1, 2, 5])) # [1, 3, 2, 5] или другой порядок
print(find_unique_numbers([1, 7, 2, 3, -1, 0, 2])) # [1, 7, 2, 3, -1, 0] или другой порядок
print(find_unique_numbers([3, 3, 3])) # [3]
