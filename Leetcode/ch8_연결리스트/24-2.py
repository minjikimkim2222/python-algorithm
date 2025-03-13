# 문제 설명 :
    # '모든 노드'의 '인전한' 노드끼리만 swap 시켜, 반환해준다.
    # 단, 노드값만 수정하는 것이 아니라, 노드 자체를 수정하는 것으로 한다.

# 문제 핵심
    # '모든' 노드에서 swap하는 스텝을 동일하게 반복하니 -> 반복문 / 재귀 떠오름
    # 24.py와 달리, 재귀를 이용하여 풀이해보자!


# 자료구조, 알고리즘
    # 자료구조 - 주어진 연결리스트
    # 알고리즘 - 재귀

# (추가) 재귀 문풀 과정
    # 1. Base Case - 재귀 종료조건 부터 생각하기
        # head 기준으로, 현재 head 노드가 없거나 / head 노드가 1개뿐이라면 swap할 2개의 노드가 없기에 종료
        # 이때, head를 리턴해줌

    # 2. 작은 문제를 해결하고, 남은 문제는 재귀가 맡긴다!
        # 예) 현재 : 1 -> 2 -> 3 -> 4 -> None (이때 first는 1, second는 2)
        #swap 이후 : 2 -> 1 -> ( ?? ) -- 여기서 ?? 부분은, 재귀호출에 의해 정렬된 것이 온다고 믿기!
        # 즉 내가 2 -> 1 swap만 작성해주면, (??)에서 정렬된 노드의 첫 head를 리턴해주어서,
        # 2 -> 1 -> ( 4 -> 3) 이 온다고 믿기!

# 시간복잡도 - 한번의 재귀호출에서 두 개의 노드를 처리하므로, O(n)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1) Base-condition : 빈 리스트거나, 노드가 1개 남은 상황
        if not head or not head.next:
            return head

        # 2) 재귀 호출
        first = head
        second = head.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second

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
input_head = [1, 2, 3, 4]
input_list = solution.to_listNode(input_head)
print_listnode(input_list)

output = solution.swapPairs(input_list)
print_listnode(output)