def count_frequency(arr):
    freq = {} # словарь частот
    for x in arr:
        if x in freq: # если уже есть элемент, то прибавляем 1
            freq[x] += 1
        else:
            freq[x] = 1 # инициализируем значение, если встретили впервые
    for key, val in freq.items():
        print(f"{key}: {val}")

count_frequency([1, 2, 3, 2, 2, 3, 3, 2]) # 1: 1, 2: 4, 3: 3