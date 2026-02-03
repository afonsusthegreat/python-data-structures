from collections import deque
data = []
data.append(5)
data.append(10)
data.pop()  # Stack / LIFO: o último elemento é removido
print(data[-1])
data.append(10)
data.append(15)  # queue
data.pop(0)  # dequeue / FIFO: o primeiro elemento é removido
print(data)
# usar listas consome muito tempo, existe solução melhor

data = deque
