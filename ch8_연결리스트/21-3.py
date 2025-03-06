

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 기저조건 - list1이 None이면..
        # 만일 list1이 list2보다 크다면 -> swap! -> 항상 list1이 list2보다 작게끔 !!
        if (not list1) or  (list2 and list1.val > list2.val):
            list1, list2 = list2, list1 # 파이썬에서의 swap !!

        if list1:
            list1.next = self.mergeTwoLists(list1.next, list2)

        return list1

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