import heapq # очередь с приоритетами

def find_k_maximums(arr, k):
    if len(arr) == 0 or k <= 0 or k > len(arr):
        return None
    
    queue = []
    for val in arr:
        heapq.heappush(queue, -val) # добавляем -val, чтобы первыми были наибольшие числа
    maximums = []
    for _ in range(k):
        maximums.append(-heapq.heappop(queue)) # возвращаем числа к прежнему виду
    return maximums

print(find_k_maximums([5, 1, 9, 3, 14, 7], k=3)) # [14, 9, 7]
print(find_k_maximums([-2, 3, -7, 0, 9, 3], k=3)) # [9, 3, 3]
print(find_k_maximums([2, 5, 6], k=5)) # None
print(find_k_maximums([], k=1)) # None
