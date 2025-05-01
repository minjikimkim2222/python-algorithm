# 문제 설명
#    M * N 의 2차원 grid 배열 /  1은 땅을 0은 물 / 1로 둘러싸인 섬의 개수를 구하세요

# 문제 핵심
    # 2차원 배열, 1은 땅 0은 물, "상하좌우"로 연결된 섬 -> dfs 힌트

# 자료구조 / 알고리즘
    # 완전탐색 - dfs -> "좌표 / 방문여부" 를 생각해줘야 한다!
    # 1. 아직 방문 안 한 땅 발견 (1) <- 현재 좌표
    # 2. 현재 좌표를 기준으로, 상하좌우에 아직 방문 안한 땅 있는지 확인
    # 3. 방문 안했으면 dfs 탐색!
    # 4. 방문 했고, 상하좌우 없으면, 다시 백트래킹! 되돌아가요

    # -> 이 흐름으로 봤을 때,
        # 현재 좌표 i, j 필요
        # 방문 여부 -> 1인지 0인지로 탐색


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0 # 섬의 개수

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return # 백트래킹

            grid[i][j] = '0' # 방문 표시

            # 상하좌우 dfs
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == "1" : # 방문 안한 땅 발견 !!
                    dfs(i, j)
                    count += 1 # 섬 개수 늘리기

        return count


solution = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
output = solution.numIslands(grid)
print(f'output :: {output}')
