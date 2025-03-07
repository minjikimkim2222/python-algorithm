# 문제 설명
    # 두 개의 non-negative list가 주어진다
    # 각 연결리스트를 역순으로 digit 숫자로 만든 뒤
    # 그 숫자끼리 더한 후,
    # 더한 값의 역순을 다시 연결리스트로 만들어서 반환해준다.

# 문제 핵심
    # 내 풀이 -> 각 과정의 뼈대를 잡고, 함수로 각 과정을 빼내었다

# 자료구조, 알고리즘
    # 자료구조 -> 동적배열 list
    # 알고리즘 -> 반복문 (반복문 종료조건 상기)

# 시간복잡도 : O(n)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 연결리스트 -> 가변배열로
        l1_arr = self.to_arr(l1)
        l2_arr = self.to_arr(l2)

        # 각 가변배열 -> 거꾸로 된 숫자로 변환
        digit1 = self.to_reverse_digit(l1_arr)
        digit2 = self.to_reverse_digit(l2_arr)

        # 두 개의 digit 합
        sum = digit1 + digit2

        # int 합을 연결리스트의 역으로 변환
        # 1) int : 807 -> list : [7, 0, 8]
        reverse_list = self.to_reverse_list(sum)

        # 2) 바꾼 list를 메서드를 이용해 연결리스트로 변환
        return self.to_linkNode(reverse_list)

    def to_reverse_list(self, sum) -> list:
        # 에외상황 : sum == 0
        if sum == 0:
            return [0]

        reverse_list = []
        while True:
            if sum // 10 == 0:
                reverse_list.append(sum % 10)
                break
            reverse_list.append(sum % 10)
            sum = sum // 10
        return reverse_list

    # 주어진 list -> 거꾸로 digit으로 변환해주는 함수
    def to_reverse_digit(self, li) -> int:
        sum = 0
        for idx, data in enumerate(li):
            ten_nums, count = 1, idx
            # ten_nums 게산 (누적 10의 제곱)
            while count > 0:
                ten_nums *= 10
                count -= 1
            sum += data * ten_nums
        return sum

    def to_arr(self, head):
        cur = head
        return_list = []

        while cur:
            return_list.append(cur.val)
            cur = cur.next
        return return_list

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
l1 = [0]
l2 = [0]
list1 = solution.to_linkNode(l1)
list2 = solution.to_linkNode(l2)
# print_linkNode(list1)
# print_linkNode(list2)

output = solution.addTwoNumbers(list1, list2)
print_linkNode(output)