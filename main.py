from collections import deque

#порожній стек
stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)