# 문제 설명
    # 연결리스트를 뒤집어서 출력하라

# 문제 핵심
    # 연결리스트 뒤집기

# 자료구조, 알고리즘
    # 검색해보니, list가 제공해주는 함수 중 reverse가 있대서..

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

        head_arr.reverse()

        # 배열 -> 연결리스트로
        return self.to_listNode(head_arr)



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
head = [1, 2, 3, 4]

head_list = solution.to_listNode(head)
print_list(head_list)

output = solution.reverseList(head_list)
print(f'output :: {output}')
print_list(output)