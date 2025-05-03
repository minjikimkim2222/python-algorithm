# 문제 설명 - 순열
    # integer배열을 입력받아, 가능한 모든 순열을 리턴하라

# 문제 핵심
    # "가능한 모든" -> 뭔가의 경우의 수, 완탐의 향기가 난다..
    # 완탐 향기 -> 트리 형식으로 그려보자!

# 자료구조, 알고리즘

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []

        len_nums = len(nums)
        ret_list = []

        # depth : 현재 탐색 깊이, discovered : 현재까지 모은 조합
        def dfs(depth, discovered):
            # 재귀 종료 조건
            if depth == len_nums:
                ret_list.append(discovered.copy()) # 반드시 복사본을 넘겨주어야, 결과 리스트에 변화없읍 !!
                print(f'재귀 종료에서의 ret_list :: {ret_list}')
                return

            # 재귀 호출 부분
            for num in nums: # 1, 2, 3
                if num not in discovered:
                    discovered.append(num) # 1 방문 표시
                    dfs(depth + 1, discovered) # dfs 다음 depth 재귀 호출
                    discovered.pop() # ** 한 depth 종류 후, 백트래킹을 해줘야, 다음 후보 탐색 가능!! **
                    print(f'재귀 완료 후, 백트래킹 :: {depth} / {discovered}')

        dfs(0, [])

        return ret_list


solution = Solution()

nums = [1, 2, 3]
output = solution.permute(nums)
print(f'output :: {output}')