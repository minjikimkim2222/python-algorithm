# 문제 설명
    # 조합 - 전체수 n을 입력받아, 가능한 k개의 조합(nCk)를 출력하라

# 문제 핵심
    # 4C2 - 1~4 중에, 2개씩 고른, '모든' 조합을 리턴하라!
    # '완탐'이니깐, dfs / bfs 고민 -> 트리구조로 조합을 그려본다.

# 자료구조, 알고리즘
    # dfs 구조에서,
    # 조합은 순서상관없이 중복을 제거해줘야 하니까, start를 이용해, 지금보다 더 큰 수를 탐색하도록 한다
    # dfs(start, combi) : 현재 combi인 상태에서, 다음 노드는 start를 탐색할거다!

# 시간복잡도

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []

        # start : 탐색을 시작할 다음 숫자
        # combi : 현재까지 완성한 조합
        def dfs(start, combi):
            # 1. 재귀 종료조건
            if len(combi) == k:
                result.append(combi[:]) # combi 깊은 복사해줘야 함!!
                return

            # 2. 재귀 호출
            for i in range(start, n + 1): # start부터 탐색하도록 함으로써, 조합에서의 중복 제거!!
                combi.append(i) # 조합에 현재 탐색한 숫자 넣기
                dfs(i + 1, combi)
                # 재귀호출 종료 후 돌아온 곳! -
                combi.pop() # 백트래킹을 위해 삭제


        dfs(1, [])

        return result


solution = Solution()
output = solution.combine(4, 2)
print(f'output :: {output}')