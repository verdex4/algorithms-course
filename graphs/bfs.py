from collections import deque

def bfs(graph, start, end):
    if start == end:
        return 0
    
    # вершина и расстояние
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        # берем первый элемент очереди
        current, distance = queue.popleft()
        
        # проверяем соседей текущей вершины
        for neighbor in graph.get(current, []):
            if neighbor == end:
                return distance + 1
            # добавляем в очередь непосещенных соседей
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    
    return -1

graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}
start = 'A'
end = 'C'
print(bfs(graph, start, end)) # 2