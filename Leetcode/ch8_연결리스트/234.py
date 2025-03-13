# 문제 설명
    # 1. 주어진 연결리스트가 팰린드롬인지 판별해서 T/F 반환
    # 2. 이때 팰린드롬이란, 앞에서 읽으니 뒤에서 읽으나 같은 순서임을 말함

# 문제 핵심
    # 팰린드롬 여부를 판단하려면, 앞/뒤로 자유자재로 인덱스에 접근할 수 있어야 하니.. -> 동적배열인 list 자료구조가 적절!
    # 연결리스트 처음/끝 접근해야 해서 -> list의 pop 사용!

# 사용할 자료구조, 알고리즘 - 동적배열 list

# 시간복잡도 :
    # 문제의 input 범위가 ~10^5, 즉 십만개라서 -> O(NlogN) 까지는 ok, 시간복잡도 : O(n) 이면 더 좋음


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head : Optional[ListNode]) -> bool:
        # 연결리스트를 동적배열로 변환
        to_list = []

        current = head
        while current:
            to_list.append(current.val)
            current = current.next


        # 배열 앞/뒤 기준으로 동일하면 pop, 동일하지 않으면 False 반환
        while len(to_list) > 1:
            if to_list.pop(0) != to_list.pop():
                return False

        # 모든 기준 통과 -> True
        return True


solution = Solution()
head = [1, 2, 3, 2, 1]
is_palindrome = solution.isPalindrome(head)
print(f'팰린드롬 여부 :: {is_palindrome}')