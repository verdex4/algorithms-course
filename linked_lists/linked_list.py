class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, arr=None):
        self.head = None
        self.length = 0

        if arr: # инициализируем списком
            for i in range(len(arr)):
                node = Node(arr[i])
                self.append(node)

    def items(self):
        """Возвращает генератор элементов"""
        if self.head is None:
            return
        
        cur = self.head
        for _ in range(self.length):
            yield cur
            cur = cur.next
    
    def __str__(self):
        """Возвращает строку в виде списка из значений элементов"""
        elements = []
        for e in self.items():
            elements.append(e.value)
        return f"{elements}"
    
    def append(self, node: Node):
        """Добавляет элемент в конец"""
        if self.head is None:
            self.head = node
            self.length += 1
            return

        cur = self.head
        for _ in range(self.length):
            if cur.next is None: # встретили последний элемент
                cur.next = node
                self.length += 1
            else:
                cur = cur.next
    
    def reverse(self):
        """Переворачивает связный список"""
        if self.head is None:
            return self
        
        prev = None
        cur = self.head
        next = self.head.next
        for _ in range(1, self.length):
            cur.next = prev # меняем ссылку
            # сдвигаем prev, cur, next
            prev = cur
            cur = next
            next = next.next

        # меняем ссылку для последнего элемента
        cur.next = prev
        self.head = cur # меняем начальный элемент

        return self