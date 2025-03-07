# 문제 설명
    # 연결리스트를 뒤집어서 출력하라

# 문제 핵심
    # 연결리스트 뒤집기

# 자료구조, 알고리즘
    # 처음 드는 생각 - 연결리스트를 list에 담은 뒤 + list배열을 거꾸로 순회하며 + 각 값을 리턴할 배열에 더해주기

# 시간복잡도 : O(n)


from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 주어진 연결리스트를 -> 배열로 변환
        head_arr = self.to_arr(head)
        return_list = []

        # 배열을 거꾸로 순회하며, 각 값을 return_list에 넣기
        for i in range(len(head_arr) - 1, -1, -1):
            return_list.append(head_arr[i])

        # 최종 리턴값 형태 맞추기 (배열 -> 연결리스트)
        return self.to_listNode(return_list)


    # 주어진 input의 배열 -> 연결리스트로
    def to_listNode(self, arr) -> ListNode:
        if not arr:
            print(f'해당 배열이 비었습니다.')
            return None
        dummy = ListNode()
        current = dummy
        for data in arr:
            current.next = ListNode(data)
            current = current.next
        return dummy.next


    # 연결리스트를 -> 가변배열, list에 담기
    def to_arr(self, head) -> list:
        current = head
        return_list = []
        while current is not None:
            return_list.append(current.val)
            current = current.next
        return return_list

def print_list(head):
    current = head
    while current is not None:
        print(f'현재 노드값 :: {current.val}')
        current = current.next

solution = Solution()
head = []

head_list = solution.to_listNode(head)
print_list(head_list)

output = solution.reverseList(head_list)
print(f'output :: {output}')
print_list(output)