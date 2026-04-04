class Node:
    def __init__(self, value, prev):
        self.value = value
        self.prev = prev

class Stack:
    def __init__(self) -> None:
        self.last = None

    def push(self, value) -> None:
        self.last = Node(value=value, prev=self.last)

    def pop(self):
        l = self.last
        if l is None:
            raise IndexError("Stack is empty")
        self.last = self.last.prev
        return l.value

    def top(self):
        if self.last is None:
            raise IndexError("Stack is empty")
        return self.last.value

    def isEmpty(self) -> bool:
        if self.last is None:
            return True
        return False
    
stack = Stack()
print(stack.isEmpty()) # True
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop()) # 3
print(stack.top()) # 2
print(stack.isEmpty()) # False