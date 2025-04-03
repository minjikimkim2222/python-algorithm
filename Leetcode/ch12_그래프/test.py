from collections import deque

queue = deque( [1,2])
queue.append(3)
print(f'queue :: {queue}')

queue.appendleft(5)
print(f'queue :: {queue}')