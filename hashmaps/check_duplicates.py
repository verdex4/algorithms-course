def check_duplicates(arr):
    seen = {} # словарь увиденных чисел
    for x in arr:
        # если уже есть элемент, он не уникальный -> есть дубликаты
        if x in seen: 
            return True
        seen[x] = True
    
    return False

print(check_duplicates([1, 2, 3, 4, 5])) # False
print(check_duplicates([1, 2, 3, 4, 2])) # True
print(check_duplicates([-1, 2, 5, 4, 1])) # False
print(check_duplicates([0])) # False