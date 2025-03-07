# 문제 설명
    # 연결리스트를 뒤집어서 출력하라

# 문제 핵심
    # 연결리스트의 방향을 뒤집으려면,
    # 1) 각 노드별로 '모두' 다음 노드를 가리키는 방향을 역순으로 바꿔줘야 함
    # 2) 앞선 과정을 모든 노드에 적용해야 한다
    # -> "동일한 과정" "여러번" 반복 !!
    # -> 반복문 or 재귀로 풀 수 있겠다 !

# 자료구조, 알고리즘
    # 1) 반복문 - 206-3에서 풀었다.
    # 2) 재귀

# 시간복잡도 :


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 기저조건
        if not head or not head.next:
            return head

        # 재귀호출
        reversed_node = self.reverseList(head.next)

        head.next.next = head # 순서 뒤바꾸기
        head.next = None # 기존 cur의 next 없애기

        return reversed_node



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