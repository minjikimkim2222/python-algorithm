# 문제 설명
    # 연결리스트의 홀수번째 노드를 입력순서대로 먼저 연결한 뒤, 그뒤를 짝수번째 노드가 잇는다
    # 제한조건 : 공간복잡도 O(1), 시간복잡도 : O(n)
        # -- 공간복잡도가 O(1) : 추가적인 메모리 사용 불가, 주어진 연결리스트를 수정해서 반환하라!

# 문제 핵심 -> 각 반복문마다 어떤 일들을 행해줘야 하는지 정확히 파악하기 (뭔가 변수가 많아진다면,, 잘못되고 있다는 신호)
    # 1) 홀수 먼저 잇기 -> odd 포인터 갱신
    # 2) 짝수끼리 잇기 -> even 포인터 갱신
    # 3) 홀수의 마지막 노드 다음에, 짝수 노드 시작 노드 잇기 (반복문 전, even_head 포인터를 저장해둬야 함!)

# 자료구조, 알고리즘
    # 자료구조 - 공간복잡도가 O(1) 이기에 주어진 연결리스트를 수정한 뒤 반환해야 함
    # 알고리즘 - 반복문

# 시간복잡도 - while문 1번, O(n)

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 예외상황 - 빈 연결리스트 (그대로 반환)
        if not head:
            return head

        # 홀수번째 시작점, 짝수번째 시작점
        odd = head
        even = head.next
        even_head = even # 짝수번째 시작노드 저장 (후에 홀수번째 노드 뒤에, 짝수 시작점과 이을 수 있게끔)
        odd_head = odd # 리턴할 홀수번째 노드의 첫 노드

        # 반복문
        while even and even.next:
            # 1) 홀수 정렬 : 1 -> 3
            odd.next = even.next
            odd = odd.next

            # 2) 짝수 정렬 : 2 -> 4
            even.next = odd.next
            even = even.next

            # 3) 홀수의 마지막 위치에, 짝수의 시작점과 잇기 ; 3 -> 2
            odd.next = even_head

        return odd_head


    # 배열 -> 연결리스트
    def to_listNode(self, arr) -> ListNode:
        if not arr:
            print('빈 배열입니다')
            return

        dummy = ListNode()
        cur = dummy

        for data in arr:
            cur.next = ListNode(data)
            cur = cur.next

        return dummy.next

def print_listNode(head):
    if not head:
        print('빈 연결리스트입니다.')
        return

    cur = head
    while cur:
        print(f'현재 노드 : {cur.val}')
        cur = cur.next

solution = Solution()
head = []
head_list = solution.to_listNode(head)
# print_listNode(head_list)
output = solution.oddEvenList(head_list)
print_listNode(output)