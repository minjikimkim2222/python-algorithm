# 문제 설명 - 조합 문제 / nCk 가능한 모든 경우의 수를 구하라

# 문제 핵심
    # 모든 경우의 수를 구하라 -> 완탐 -> dfs -> 트리구조를 그려보자!
    # 모르겠는 지점, [2]까지 고른 상황에서 [2,1]은 [1,2]로 인해서 안하는데 그걸 어떻게 안하지?

    # 즉, 중복을 어떻게 제거할까? -- start 인덱스 사용
        # 다음 숫자를 선택할 때는, "이전 숫자"보다 "더 큰" 숫자만 선택하도록 한다 **
        # 이를 위해 매 재귀호출마다, start 값을 넘겨준다
        # for i in range(start, n+1) --> 이렇게 하면, 숫자는 항상 오름차순만 뽑혀서 중복 불가

# 자료구조 / 알고리즘

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        if n == 1 and k == 1:
            return [[1]]

        ret_list = []

        def dfs(start, discovered):
            # 재귀 종료조건
            if len(discovered) == k: # k개수를 다 모았다면
                ret_list.append(discovered.copy()) # copy본을 넘거야, 원본 discovered를 못 넘김
                return

            # 재귀 호출 부분
            #for i in range(1, n + 1): # 1, 2, 3, 4
            for i in range(start, n + 1):
                discovered.append(i)
                dfs(i + 1, discovered)
                discovered.pop() # 재귀 종료 후, 백트래킹을 위해 pop

        dfs(1, [])

        return ret_list



solution = Solution()
n, k = 4, 2
output = solution.combine(n, k)
print(f'output :: {output}')

