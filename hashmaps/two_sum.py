def two_sum(arr, target):
    seen = {} # словарь уже встреченных значений; number: index
    for idx, cur in enumerate(arr):
        required_num = target - cur # ищем пару к текущему: cur + required_num = target

        # если уже есть необходимый, возвращаем индексы элементов
        if required_num in seen:
            return [seen[required_num], idx]
        
        # если не нашли, то добавляем кандидата в словарь
        seen[cur] = idx
    
    return -1

print(two_sum([2, 7, 11, 15], 9)) # [0, 1]
print(two_sum([1, 4, 8, 3, 7, 15], 7)) # [1, 3]
print(two_sum([5, 8, 4], 6)) # -1
