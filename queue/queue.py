class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Queue:
    def __init__(self) -> None:
        self.first = None
        self.last = None

    def enqueue(self, value):
        cur = Node(value, None)
        prev = self.last
        self.last = cur
        if prev is None:
            self.first = cur
            return
        prev.next = cur

    def dequeue(self):
        f = self.first
        if f is None:
            raise IndexError("Queue is empty")
        self.first = self.first.next
        return f.value

    def front(self):
        if self.first is None:
            raise IndexError("Queue is empty")
        return self.first.value

    def isEmpty(self):
        if self.first is None:
            return True
        return False
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue()) # 1
print(queue.dequeue()) # 2
print(queue.front()) # 3
print(queue.isEmpty()) # False