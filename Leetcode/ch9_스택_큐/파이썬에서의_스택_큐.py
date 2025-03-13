# 파이썬에서는 가변배열 list로 스택에서 제공해주는 push, pop / 큐에서 제공하는 enqueue, dequeue 연산을 실행할 수 있다!

## 1. list로 stack 연산 사용해보기
stack = []
stack.append(1) # push(1)
stack.append(2) # push(2)
stack.append(3) # push(3)

print(stack.pop()) # 3 (후입선출)
print(stack.pop()) # 2
print(stack.pop()) # 1

## 2. list로 queue 연산 사용해보기
queue = []
queue.append(1) # 마치 enqueue(1)과 같다
queue.append(2)
queue.append(3)

print(queue.pop(0)) # pop(0)으로 dequeue와 동일하게 동작하게끔 한다.
print(queue.pop(0))
print(queue.pop(0))

## 3. 하지만, 큐 연산을 사용할 때는 list보다는 Deque가 성능상 더 좋다
from collections import deque

queue = deque()
queue.append(1) # 마찬가지로 enqueue(1)과 동일한 연산을 수행함
queue.append(2)
queue.append(3)

print(queue.popleft()) # 1 , 데크는 pop() 대신 popleft()를 사용한다
print(queue.popleft())
print(queue.popleft())

### 번외, 물론 deque에서 pop()도 사용가능한데, deque.pop()을 사용하면, 오른쪽에서 제거된다
dq = deque()
dq.append(1)
dq.append(2)
dq.append(3)

print(dq.pop()) # 3, 오른쪽에서 제거됨
print(dq.popleft()) # 1, 왼쪽에서 제거됨
print(dq.pop()) # 2, 오른쪽에서 제거됨

import collections

num = ['one', 'two', 'two', 'three', 'three', 'three', 'four']
counter = collections.Counter(num)
max_counter = counter.most_common(2)

deque = collections.deque()