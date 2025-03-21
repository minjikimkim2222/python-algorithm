# 문제 설명
    # 다음 연산을 제공하는 '원형' '데크'를 구현해봐라
from symbol import trailer


# 문제 핵심
    # 배열을 이용하면, 삽입/삭제 시 시간복잡도가 O(n)으로 비효율적이기에,
    # 연결리스트로 구현해본다.

# 자료구조, 알고리즘
    # 맨앞쪽 노드를 가리키는 head, 맨 뒤 노드를 가리키는 tail 노드로 인해, 이중연결리스트 로 구현해보고자 한다

# 시간복잡도



# 이중연결리스트의 노드
class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

# 원형 데크 구현 -> 이중연결리스트
class MyCircularDeque:

    # 왼쪽,오른쪽 인덱스의 head,tail 노드 / 최대 길이 정보 k / 현재 길이 정보 len
    def __init__(self, k: int):
        self.head, self.tail = Node(None), Node(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 맨 앞에 노드 추가
    def insertFront(self, value: int) -> bool:
        if self.len == self.k:
            return False # 최대 길이에 도달하면, 더이상 넣지 못함

        new_node = Node(value)

        first = self.head.right
        self.head.right = new_node
        new_node.left, new_node.right = self.head, first
        first.left = new_node

        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False

        new_node = Node(value)
        last = self.tail.left

        self.tail.left = new_node
        new_node.right, new_node.left = self.tail, last
        last.right = new_node

        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False # 비어 있으면 삭제 불가

        first = self.head.right
        self.head.right = first.right
        first.right.left = self.head

        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False

        last = self.tail.left
        self.tail.left = last.left
        last.left.right = self.tail

        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.len > 0:
            return self.head.right.val
        return -1

    def getRear(self) -> int:
        if self.len > 0:
            return self.tail.left.val
        return -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k

def print_node(head):
    if head is None or head.right == head:
        print(f'빈 데크입니다.')
        return

    current = head.right
    while current != head: # head를 다시 만나면 종료
        print(current.val)
        current = current.right
    print('*** end ***')

obj = MyCircularDeque(3)
obj.insertFront(1)
print_node(obj.head)