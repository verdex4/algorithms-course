def find_max_sorted(arr):
    if len(arr) == 0:
        return None
    
    return arr[-1]

print(find_max_sorted([1, 4, 6, 9, 15])) # 15
print(find_max_sorted([-10, -4, -32, -1, 0, 9])) # 9
print(find_max_sorted([])) # None