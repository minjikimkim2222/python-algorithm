# 문제 설명 / 핵심 - 큐를 이용한 스택 구현

# 자료구조, 알고리즘 - 파이썬의 큐, collections.deque 활용 + 큐의 FIFO 연산만 활용해서 구현한다
    # deque의 append
    # deque의 popleft, pop

    # ** 큐의 FIFO 연산만 가지고 -> 스택을 구현한다 !

# 시간복잡도

from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque() # collections의 deque 선언

    def push(self, x: int) -> None:
        self.queue.append(x)

        # 후에 pop에서 popleft로 공간 상 가장 왼쪽것을 빼니까,
        # 요소 삽입 후, 방금 삽입한 요소를 맨 앞으로 끼워넣는 상태로 재정렬 **
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int: # 문제조건상, 데크의 FIFO pop 연산인, popleft()로 제한한다..
        if not self.empty():
            data = self.queue.popleft()
            return data

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

def print_stack(stack):
    for i in range(len(stack.queue)):
        print(stack.queue[i])

myStack = MyStack()
myStack.push(1) # 1
myStack.push(2) # 1 2
print(myStack.top()) # 2
print(myStack.pop()) # return 2, pop
print(myStack.empty()) # False

# myStack.top() # return 2
# myStack.pop() # return 2 + pop 연산
# myStack.empty() # return False