# 문제 설명
    # k개의 정렬된 리스트를 -> 1개의 정렬된 리스트로 병합하라

# 문제 핵심
    # 각 리스트가 정렬된 상태라, 각 리스트의 '가장 작은 값'을 하나씩 병합하면 된다!
    # 즉, 각 리스트의 최소값을 빠르게 뽑아내야 한다! -> 최소 우선순위 큐

# 자료구조, 알고리즘
    # 최소 우선순위 큐

# 시간복잡도

from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [] # 최소 우선순위 큐

        # 각 리스트의 첫번째 노드만 힙에 추가
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i, l)) # (값, 인덱스, 노드)

        dummy = ListNode()
        cur = dummy

        # 우선순위 큐에서 가장 작은 값을 하나씩 꺼내어 연결!
        while pq:
            val, idx, node = heapq.heappop(pq)
            cur.next = ListNode(val)
            cur = cur.next

            # 빠진 노드 기준, 다음 노드가 있다면 최소 우선순위 큐에 넣기
            if node.next:
                heapq.heappush(pq, (node.next.val, idx,  node.next))

        return dummy.next


def array_to_linked_list(arr):
    dummy = ListNode()
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

def print_listnode(head):
    cur = head

    while cur:
        print(cur.val)
        cur = cur.next

solution = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]

listnodes = [array_to_linked_list(lst) for lst in lists]

head = solution.mergeKLists(listnodes)
print_listnode(head)