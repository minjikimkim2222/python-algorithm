# 문제 설명 - (#225 문제와 반대로) 스택 연산을 이용해 -> 큐를 만들 것

# 문제 핵심 - 스택의 append(), pop() 연산만 사용해서, 큐를 만드는 것
    # 스택의 후입선출 만 사용해서 -> 큐의 선입선출을 구현하는 것
    # 스택의 연산만으로 어떻게 먼저 들어온 원소를 가장 먼저 나오게 할 것인가?

    # FIFO를 만들려면, 한번은 순서를 뒤집어야 한다
        # 스택 1개로 뒤집으면, 순서를 유지할 수 없음
        # 따라서 스택 2개로 하나를 거꾸로 뒤집어서 FIFO 흉내내기

# 자료구조, 알고리즘

# 시간복잡도

class MyQueue:

    def __init__(self):
        self.in_stack = [] # [1,2,3] 순서대로 저장됨
        self.out_stack = [] # [3,2,1] 순서로 뒤집어서, stack의 pop으로 큐의 선입선출 특징을 지킨다 (1 추출)

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move_in_stack_to_out_stack() # in_stack의 순서를 뒤집어서, out_stack에 저장
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move_in_stack_to_out_stack()
        return self.out_stack[-1]

    # in_stack은 큐의 입력순서를 유지하기만 하고, out_stack에서 pop연산을 통해 값을 내보내므로..
    def empty(self) -> bool:
        return len(self.out_stack) == 0 and len(self.in_stack) == 0

    def move_in_stack_to_out_stack(self):
        if not self.out_stack: # out_stack이 비어있을 때만.. (비어있지 않다면, 이미 정렬된 상태라 굳이)
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

myqueue = MyQueue()
myqueue.push(1)
myqueue.push(2)
print(myqueue.peek()) # return 1
print(myqueue.pop()) # return 1, queue is [2]

print(myqueue.empty()) # return False