# 연결리스트를 이용해 스택 연산 push, pop을 구현해보자
# 스택은 LIFO이기에 1,2,3을 넣는다고 가정하면, 3 -> 2 -> 1 의 연결리스트가 만들어진다.



# 연결리스트의 Node 정의
class Node:
    def __init__(self, item=0, next=None):
        self.item = item
        self.next = next

# Stack 클래스 정의
class Stack:
    def __init__(self):
        self.last = None # 포인터 last는 가장 마지막 요소(top)를 가리킨다.

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.last
        self.last = new_node

    def pop(self) -> int:
        if not self.last:
            return None # 스택이 비어있어서, pop할 요소가 없음
        item = self.last.item # pop하기 전, item 요소 저장
        self.last = self.last.next # last는 이전 요소를 가리키도록 이동
        return item

# Stack 사용 예제
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.pop())  # None (스택이 비었음)
print(stack)
