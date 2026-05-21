def x_maximums(arr, x):
    if x <= 0 or x > len(arr):
        return []
    
    # строим минимальную кучу из первых x элементов
    heap = arr[:x]
    build_min_heap(heap)
    
    # проходим по остальным
    for i in range(x, len(arr)):
        # в минимальной куче первый элемент всегда минимальный
        if arr[i] > heap[0]:
            heap[0] = arr[i]
            # восстанавливаем свойство кучи
            sift_down(heap, 0, len(heap))
    
    # сортируем, т.к. получили x неотсортированных максимумов
    return sorted(heap, reverse=True)

def build_min_heap(arr):
    n = len(arr)
    start = (n - 2) // 2 
    for i in range(start, -1, -1):
        sift_down(arr, i, n)

def sift_down(heap, idx, size):
    while True:
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx
        
        if left < size and heap[left] < heap[smallest]:
            smallest = left
            
        if right < size and heap[right] < heap[smallest]:
            smallest = right
            
        # если наименьший элемент изменился, меняем местами и продолжаем
        if smallest != idx:
            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
        else:
            break

arr = [5, 1, 9, 3, 14, 7]
x = 3
print(x_maximums(arr, x)) # [14, 9, 7]