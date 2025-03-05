# 연결리스트에는 3가지 종류가 있다 - 단순, 원형, 이중 연결리스트
# 연결리스트는 (데이터값 + 링크)로 구성된 노드로 이루어져있다. 이때 링크는 포인터로 구현되어 다른 노드를 참조하게 된다

# 연결리스트 종류
# 1. 단순 연결 리스트 :
    # 단순 연결 리스트는 헤더 노드가 존재하며 + 헤더 노드는 다음 노드를 그리고 다음 노드는 그 다음 노드를 가리킨다.
    # 한 방향으로 연결되어 단순 연결 리스트라고 부른다.
# 2. 원형 연결 리스트 :
    # 단순 연결 리스트와 대부분 동일하지만,
    # tail 노드가 head 노드를 가리키고 있다는 점이 다르다.
# 3. 이중 연결 리스트
    # 이중 연결리스트는 헤더 노드만 존재하며,
    # 각 노드는 다음 노드를 가리킴과 동시에 이전노드를 가리키는 링크를 가지고 있다.

# 노드 생성 with Python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    # 이때, __init__은 파이썬 클래스에서 생성자 역할. 객체가 생성될 때 자동으로 호출되어 초기화해줌
head = Node(5)
next_node = Node(3)
head.next = next_node

# 연결리스트 순회함수
def traverse(head):
    current = head
    while current is not None: # 현재 노드
        print(f'현재 노드 값 :: {current.data}')
        current = current.next
traverse(head)

print(f' *** 예제 구분 **** ')
# 단순 연결리스트 정의 with Python
    # 구현할 항목들
    # 1. 첫번째 노드 삽입
    # 2. 중간 노드 삽입
    # 3. 마지막 노드 삽입
    # 4. 노드 삭제

# Node 생성 클래스
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 단순연결리스트 클래스 -> 헤더노드가 존재한다 (필수), 편의상 리스트 크기 변수
class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)  # 첫 노드 생성
        self.head = new_node   # head가 첫 노드를 가리킴
        self.list_size = 1     # 리스트크기 초기화

    # 1. 첫번째(헤드) 노드 삽입 - 첫번째 위치에 삽입
    def insert_first(self, data):
        insert_node = Node(data)       # 새 노드 생성
        insert_node.next = self.head   # 새 노드의 next를 기존 head로 설정
        self.head = insert_node        # head를 새 노드로 변경

        self.list_size += 1            # 리스트 크기 증가

    # 2. 중간(특정 위치 삽입) - 지정된 위치에 삽입 *
    def insert_position(self, data, position):
        if position <= 0:
            print(f'잘못된 위치입니다')
            return

        if position == 1:
            self.insert_first(data)
            return

        new_node = Node(data)
        current = self.head
        count = 1

        # ** 삽입위치 바로 앞까지 이동 !! **
        while count < position - 1:
            count += 1
            current = current.next # 삽입 직전 위치 노드

        if current is None: # 범위 초과 처리
            print('위치가 범위를 넘어섰습니다.')
            return

        new_node.next = current.next
        current.next = new_node

        self.list_size += 1

    # 3. 마지막 노드 삽입 -> 마지막에 삽입
    def insert_last(self, data):
        last_node = Node(data)

        # 리스트가 비어있다면 (예외)
        if self.head is None:
            self.head = last_node
            return

        # 마지막 노드까지 연결리스트 탐색
        current = self.head
        while current.next is not None:
            print(f'현재 노드 데이터 :: {current.data}')
            current = current.next

        # 마지막 노드를 last_node로 연결
        current.next = last_node
        self.list_size += 1

    # 4. 노드 삭제 - 주어진 값을 가진 노드 삭제
    def delete_node(self, key):
        current = self.head
        before = None

        # (예외상황) 삭제할 노드가 헤드인 경우
        if current.data == key and current:
            self.head = current.next
            del current # 공간 낭비 방지를 위해, 완전히 삭제까지
            self.list_size -= 1
            return

        # 삭제할 노드 탐색 (전체가 아니고, key를 찾을 때까지)
        while current and current.data != key:
            before = current
            current = current.next

        # (예외 상황) 찾는 key가 존재하지 않는다면..
        if current is None:
            print(f'현재 찾는 키가 존재하지 않습니다.')
            return
        before.next = current.next
        del current # 완전 삭제
        self.list_size -= 1

    # 모든 노드 출력
    def print_all_nodes(self, head):
        current = head
        while current is not None:
            print(f'현재 노드 값 :: {current.data}')
            current = current.next

# 테스트 코드
sli = SingleLinkedList(10)
sli.insert_first(3) # 3 -> 10
sli.insert_position(5, 2) # 두번째 노드 위치에 삽입한다
sli.print_all_nodes(sli.head) # 3 -> 5 -> 10
print(f'현재 연결리스트 크기 :: {sli.list_size}')

sli.insert_last(77)
sli.print_all_nodes(sli.head)

print(f'노드 삭제 이후 !!')
sli.delete_node(5)
sli.print_all_nodes(sli.head)