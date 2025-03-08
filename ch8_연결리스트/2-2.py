# 문제 설명
    # 두 개의 non-negative list가 주어진다
    # 각 연결리스트를 역순으로 digit 숫자로 만든 뒤
    # 그 숫자끼리 더한 후,
    # 더한 값의 역순을 다시 연결리스트로 만들어서 반환해준다.

# 문제 핵심
    # 일일이 자료형을 변환해가며, 모든 각 과정을 구현하는 것은 이 문제가 원했던 본질이 아니었을 것이다.
    # 두번째 풀이
        # 자료형 변환없이 연결리스트를 유지한 상태에서,
        # 각 자리수별 덧셈 과정 분석 -> 전가산기(Full Adder) 방식
        # 이때, 전가산기 방식이란, 자리수를 하나씩 계산하며 + carry를 관리하는 방식!
            # 현재 자리 값 (sum) : 현재 자리 두 숫자의 합 + 이전 carry 값
            # 올림값(carry) : 만일 sum >= 10이면, 1 (== sum // 10)
            # 새로운 노드의 값 : sum의 1의 자리 (== sum % 10)


# 자료구조, 알고리즘
    # 자료구조 - 연결리스트 사용
    # 알고리즘 - 전가산기 방식 응용


# 시간복잡도 : O(n)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0 # 이전 올림값은 항상 0부터 시작

        while l1 or l2 or carry: # l1값이 있거나, l2값이 있거나 이전 올림값이 있을 때마다 반복
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            sum = val1 + val2 + carry
            new_val = sum % 10 # 나머지 -> 새로운 값
            carry = sum // 10 # 몫 -> 새로운 carry(자릿수) 값

            cur.next = ListNode(new_val)
            cur = cur.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next





    def to_linkNode(self, arr):
        dummy = ListNode()
        current = dummy
        for data in arr:
            current.next = ListNode(data)
            current = current.next
        return dummy.next

def print_linkNode(head):
    current = head
    while current:
        print(f'현재 노드 :: {current.val}')
        current = current.next

solution = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
list1 = solution.to_linkNode(l1)
list2 = solution.to_linkNode(l2)
# print_linkNode(list1)
# print_linkNode(list2)

output = solution.addTwoNumbers(list1, list2)
print_linkNode(output)