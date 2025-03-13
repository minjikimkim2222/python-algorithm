# 문제 설명
    # 연결리스트를 뒤집어서 출력하라

# 문제 핵심
    # 연결리스트의 방향을 뒤집으려면,
    # 1) 각 노드별로 '모두' 다음 노드를 가리키는 방향을 역순으로 바꿔줘야 함
    # 2) 앞선 과정을 모든 노드에 적용해야 한다
    # -> 반복문 or 재귀로 풀 수 있겠다 !

# 자료구조, 알고리즘
    # 1) 반복문 - 순차적으로 모든 노드를 방문하며, 동일한 과정을 반복해준다.
    # 2) 재귀 - 반복문과 동일한 로직으로 206-4에서 푼다.

# 시간복잡도 : O(n)


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        # cur 가 None이 아닐 때까지 반복문
        while cur:
            next_node = cur.next # 기존 cur의 next node 값 저장 !!
            cur.next = prev
            prev = cur
            cur = next_node

        return prev


    # 주어진 input의 배열 -> 연결리스트로
    def to_listNode(self, arr) -> ListNode:
        if not arr:
            print(f'해당 배열이 비었습니다.')
            return None
        dummy = ListNode()
        current = dummy
        for data in arr:
            current.next = ListNode(data)
            current = current.next
        return dummy.next


def print_list(head):
    current = head
    while current is not None:
        print(f'현재 노드값 :: {current.val}')
        current = current.next

solution = Solution()
head = [1, 2, 3, 4]

head_list = solution.to_listNode(head)
print_list(head_list)

output = solution.reverseList(head_list)
print(f'output :: {output}')
print_list(output)