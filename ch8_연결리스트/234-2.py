from typing import Optional
import collections
# 첫번째 위치를 pop()할 때 동적'배열'은 성능상 좋지 않은 자료구조이다.
# 첫번째 값을 꺼내오면 모든 값을 한 칸 앞으로 shifting되므로, 시간복잡도 O(n)이 발생하기 때문이다.
# 따라서, 조금 더 최적화된 자료구조를 사용하려면, 맨앞/맨뒤인 양쪽 방향에서 pop하기에 O(1)만큼 걸리는 deque가 효율적일 것이다.

# Collections.deque는 이중 '연결리스트'로 구현되어 있어,
# 삽입/삭제할 위치(인덱스)만 알면, pop할 때 O(1)만큼의 시간복잡도만 걸린다.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head : Optional[ListNode]) -> bool:
        # 연결리스트를 동적배열로 변환
        to_deque = collections.deque()

        current = head
        while current:
            to_deque.append(current.val)
            current = current.next


        # 배열 앞/뒤 기준으로 동일하면 pop, 동일하지 않으면 False 반환
        while len(to_deque) > 1:
            if to_deque.popleft() != to_deque.pop():
                return False

        # 모든 기준 통과 -> True
        return True
