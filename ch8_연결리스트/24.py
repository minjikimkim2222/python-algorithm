# 문제 설명 :
    # '모든 노드'의 '인전한' 노드끼리만 swap 시켜, 반환해준다.
    # 단, 노드값만 수정하는 것이 아니라, 노드 자체를 수정하는 것으로 한다.

# 문제 핵심
    # '모든' 노드에서 swap하는 스텝을 동일하게 반복하니 -> 반복문 / 재귀 떠오름
    # 반복문 선택 -> 반복 종료 범위 + 각 스텝마다 반복하는 행위 정리!
        # 1) prev.next = second (이전 노드가, 두번째 노드를 가리키도록 -> 왜냐, swap되어 바뀔 두 번째 노드를 가리켜야 하니까..)
        # 2) first.next = second.next (첫번째 노드는, 원래 두번째 노드의 다음을 가리키도록 -> 그 다음번은 swap되지 않아서, 순서 유지)
        # 3) second.next = first (swap!)


# 자료구조, 알고리즘
    # 자료구조 - 주어진 연결리스트
    # 알고리즘 - 반복문

# 시간복잡도 - O(n)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외 상황 (빈 리스트거나 노드가 하나인 경우, 그대로 반환)
        if not head or not head.next:
            return head

        # 반환할 연결리스트 생성
        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head

        # 반복문 (홀수개 종료조건까지 생각)
        while cur and cur.next:
            # swap할 두 노드
            first = cur
            second = cur.next

            # swap시키기
            prev.next = second
            first.next = second.next
            second.next = first

            # prev, cur 이동
            prev = first
            cur = first.next


        return dummy.next # 인전합 두 연결리스트끼리 swap한 결과 리턴


    # 배열 -> 연결리스트
    def to_listNode(self, arr) -> ListNode:
        if not arr:
            print(f'빈 배열입니다.')
            return
        dummy = ListNode()
        cur = dummy
        for data in arr:
            cur.next = ListNode(data)
            cur = cur.next
        return dummy.next

def print_listnode(head):
    cur = head
    while cur:
        print(f'현재 노드값 :: {cur.val}')
        cur = cur.next

solution = Solution()
input_head = [1, 2, 3]
input_list = solution.to_listNode(input_head)
print_listnode(input_list)

output = solution.swapPairs(input_list)
print_listnode(output)