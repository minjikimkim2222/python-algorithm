# 문제상황 -> 서로 다른 두 연결리스트를 합쳐서 + 정렬하라!

# 문제핵심 -> 리스트에서 제공해주는 sort 사용

# 자료구조, 알고리즘 -> 가변배열 list의 sort()를 사용하자!

# 시간복잡도 -> O(n) + O(n) + O(n log n) + O(n) => O(n log n)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 연결리스트 -> 가변배열 list
        list1_arr, list2_arr = [], []
        current1, current2 = list1, list2

        while current1 is not None:
            list1_arr.append(current1.val)
            current1 = current1.next
        while current2 is not None:
            list2_arr.append(current2.val)
            current2 = current2.next

        # merge_arr에 list1, list2를 모두 넣고 정렬
        merge_arr = []
        for data in list1_arr:
            merge_arr.append(data)
        for data in list2_arr:
            merge_arr.append(data)

        merge_arr.sort() # 리스트 정렬 -> O(n log n)

        # 리턴값 맞추기
        return self.to_linkNode(merge_arr)

    # 테스트용 함수 (배열 -> 연결리스트)
    def to_linkNode(self, arr) -> ListNode:
        dummy = ListNode()
        current = dummy
        for data in arr:
            current.next = ListNode(data)
            current = current.next
        return dummy.next

def print_linkNode(head_node):
    current = head_node

    while current is not None:
        print(f'current : {current.val}')
        current = current.next

# 테스트코드
list1 = []
list2 = [0]

solution = Solution()
listNode1 = solution.to_linkNode(list1)
listNode2 = solution.to_linkNode(list2)
# print_linkNode(listNode1)
# print_linkNode(listNode2)

output = solution.mergeTwoLists(listNode1, listNode2)
print(f'output :: {output}')