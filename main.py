#стек за допомогою класів

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Стек пустий!"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Стек пустий!"

    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.size())
print(stack.pop())
print(stack.peek())