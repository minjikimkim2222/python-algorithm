# 문제 상황
    # 2개의 정렬된 list를 input으로 받고, 다시 1개의 정렬된 리스트로 반환해주세요

# 문제 핵심
    # 각 2개의 list의 값을 비교할 때, 같으면 2개 list 인덱스 모두 증가하고,
    #                           다르면 값이 더 작은 list의 인덱스만 증가시킨다
    # 언제까지? -- 더 작은 쪽의 list가 끝날 때까지(값이 없을때까지) / 이때 다른쪽 리스트의 값이 남았다면 이어 붙이기

# 자료구조, 알고리즘
    # 서로 다른 리스트의 '인덱스'로 값 조회 -> 가변배열, list

# 시간복잡도 -> 입력범위 50개, O(2^n)까지도 OK

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge_arr = []

        # 연결리스트를 -> 배열로
        list1_arr = []
        list2_arr = []

        current1 = list1
        while current1 is not None:
            list1_arr.append(current1.val)
            current1 = current1.next

        current2 = list2
        while current2 is not None:
            list2_arr.append(current2.val)
            current2 = current2.next

        # 예외 상황 - 둘 중 하나가 빈 배열이면
        if list1_arr == [] and list2_arr == []:
            return None

        if list1_arr == [] or list2_arr == []:
            if list1_arr == []:
                return self.create_listNode(list2_arr)
            else:
                return self.create_listNode(list1_arr)

        # 각 2개 리스트 포인터 탐색
        idx1, idx2 = 0, 0
        while idx1 < len(list1_arr) and idx2 < len(list2_arr):
            if list1_arr[idx1] == list2_arr[idx2]:
                merge_arr.append(list1_arr[idx1])
                merge_arr.append(list2_arr[idx2])
                idx1 += 1
                idx2 += 1

            elif list1_arr[idx1] < list2_arr[idx2]:
                merge_arr.append(list1_arr[idx1])
                idx1 += 1

            else: # list2의 값이 더 작다면
                merge_arr.append(list2_arr[idx2])
                idx2 += 1

        # 만일 더 큰 리스트의 개수가 남았다면, 그 큰 리스트를 이어붙인다
        if idx2 == len(list2_arr): # list1의 개수가 남았음 - 남은 list1 을 이어붙인다
            for data in list1_arr[idx1:]:
                merge_arr.append(data)

        if idx1 == len(list1_arr): # list2의 개수가 남았음 - 남은 list2를 이어붙인다
            for data in list2_arr[idx2:]:
                merge_arr.append(data)

        # 리턴값 맞추기 (배열 -> 연결리스트)
        return self.create_listNode(merge_arr)


    # 테스트용 함수 (배열 -> 연결리스트로 채우기)
    def create_listNode(self, arr) -> ListNode:
        if len(arr) == 0:
            print(f'리스트가 빈 배열입니다.')
            return None

        dummy = ListNode() # 더미 노드 생성
        current = dummy
        for data in arr:
            current.next = ListNode(data)
            current = current.next

        return dummy.next # 더미 노드의 next 반환 (진짜 head)

    # 테스트용 함수 (연결리스트 출력)
    def print_listNode(self, head_node):
        current = head_node

        while current is not None:
            print(f'현재 노드 : {current.val}')
            current = current.next


# 테스트
solution = Solution()
list1 = [1, 3, 4]
list2 = [1, 5, 6]

linked_list1 = solution.create_listNode(list1)
# solution.print_listNode(linked_list1) # list1 연결리스트 출력
linked_list2 = solution.create_listNode(list2)
# solution.print_listNode(linked_list2)
output = solution.mergeTwoLists(linked_list1, linked_list2)

print(f'output :: {output}')