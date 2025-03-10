# 문제 설명 - 연결리스트 부분 reverse
    # left ~ right 까지 만 reverse한 뒤, 연결리스트 반환

# 문제 핵심
    # 연결리스트에서 left ~ right 사이 부분만 뒤집고, 나머지는 유지한 채 새로운 리스트 반환
    # 단순 배열이라면 arr[left:right+1].reverse()로 간단히 처리할 수 있겠으나, 연결리스트를 인덱스를 통한 접근이 불가하다

    # 따라서 앞에서부터 left까지 이동하고, 해당 구간을 뒤집은 후  + 다시 이어주는 과정이 필요하다!

# 자료구조, 알고리즘
    # 자료구조 - 주어진 연결리스트
    # 알고리즘 - 반복문

# 시간복잡도 -> O(n)


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 예외 상황 : left와 right가 동일한 순간 - 뒤집을 필요가 없음 (그대로 리턴)
        if not head or left == right:
            return head

        # 더미노드를 활용해, 시작부분을 관리하기 쉽도록 한다
        dummy = ListNode(0, head) # 더미노드로 reverse되는 부분 연결리스트를 채워넣어, 반환하기 쉽게끔 한다
        prev = dummy

        # prev를 left 직전 노드로 이동, cur는 left를 가리킨다
        for _ in range(left - 1):
            prev = prev.next
        cur = prev.next

        # left ~ right 까지의 구간 뒤집기 - 예) 1->2->3->4->5에서 1->3->2->4->5 / 그다음 1->4->3->2->5
        for _ in range(0, right - left):
            temp = cur.next

            cur.next = temp.next # 1) 2 -> 4 [여기서 cur.next가 갱신된 것을 조심할 것..]
            temp.next = prev.next # 2) 3 -> 2
            prev.next = temp # 3) 1)과 2) 사이를 잇는다 ; 1 -> 3


        return dummy.next



    # 배열 -> 연결리스트
    def to_listNode(self, arr) -> ListNode:
        if not arr:
            print('빈 배열입니다.')
            return
        dummy = ListNode()
        cur = dummy
        for data in arr:
            cur.next = ListNode(data)
            cur = cur.next
        return dummy.next

def print_listNode(head):
    if not head:
        print(f'빈 연결리스트입니다')
        return
    cur = head
    while cur:
        print(f'현재 노드 : {cur.val}')
        cur = cur.next

solution = Solution()
head = [1,2,3,4,5]
head_list = solution.to_listNode(head)
# print_listNode(head_list)

left, right = 2, 5
output = solution.reverseBetween(head_list, left, right)
print_listNode(output)