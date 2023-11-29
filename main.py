from queue import LifoQueue

stack = LifoQueue(maxsize=3)
print(stack.qsize())#кількість елементів
stack.put("a")
stack.put("b")
stack.put("c")

print(stack.full())
print(stack.qsize())#кількість елементів
for i in range(stack.qsize()):
    print(stack.get())