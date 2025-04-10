# 문제 설명  - 순열
    # 서로 다른 정수를 입력받아 -> 가능한 모든 순열을 리턴하라

# 문제 핵심
    # 모든 경우의 수 탐색 -> 완탐
    # 2차원 배열 -> '트리구조'로 생각해보자
    # DFS 생각!

# 자료구조, 알고리즘

# 시간복잡도

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ret = []

        # path : 지금까지 만든 조합 (최종적으로 순열을 완성하기 위함)
        # used : 이미 선택한 데이터 (중복 없이 저장 -> set !)
        def dfs(path, used):
            # 1. 재귀 종료 조건
            if len(nums) == len(path):
                ret.append(path[:]) # 얕은 복사가 아닌, 깊은 복사를 해줘야 함!, path를 복사한 새로운 리스트
                return

            # 2. 재귀 호출 부분
            for num in nums: # num : 1, 2, 3
                if num not in used:
                    path.append(num)
                    used.add(num)

                    dfs(path, used) # dfs 호출 !!

                    # dfs 끝나고 돌아오면, 백트래킹을 위해 !!
                    path.pop()
                    used.remove(num)

        dfs([], set())

        return ret



solution = Solution()
input = [1, 2, 3]
output = solution.permute(input)
print(f'output :: {output}')