# 문제 설명 - 섬의 개수
    # 1을 육지로, 0을 물로 가정한 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라
    # 상하좌우로 연결된, 땅들의 덩어리(섬) 의 개수를 구하라!
from operator import truediv


# 문제 핵심
    # 일단 2차원 배열이 주어지고 + 연결된 데이터(1)을 하나의 그룹처럼 취급 -> 그래프 탐색 (dfs, bfs) 를 써야 겠군!
    # 근데, 이 문제 핵심이 bfs처럼 최단거리를 찾는 것이 아니라,
    # 모든 노드의 방문여부를 판단해서 + 연관된 1을 모두 방문했다면, 섬 개수 +1 이라, -> DFS 선택!

    # -> 2차원 배열을 순회하며, "아직 방문하지 않은" "땅(1)" 이 보이면, DFS로 연관된 모든 땅을 방문 처리한뒤,
    #    마무리차원으로, 섬의 개수를 +1 해서 세준다!

# 자료구조, 알고리즘 - DFS
    # 1. 2중 for문으로 전체 grid를 탐색해준다
    # 2. 이때 만약, grid[i][j] == '1' 이면 -> 아직 '방문하지 안 한' 땅이다!
    # 3. 그 지점에서 DFS를 시작해서, 연결된 "상하좌우" 모두 '1'을 '0'으로 바꿔준다 (방문표시)
    # 4. DFS 호출이 완전히 끝나면, 섬의 개수를 +1을 해준다

# 시간복잡도

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0 # 섬의 개수

        def dfs(i, j):
            # if - 재귀 종료조건 (범위를 벗어나거나, 땅이 아닌 물('0')을 만난다면..)
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0':
                return

            # 재귀호출 -> 해당 노드 방문표시 이후, 해당 노드 기준 '상하좌우' DFS 탐색
            grid[i][j] = '0' # 방문표시

            dfs(i - 1, j) # 상
            dfs(i + 1, j) # 하
            dfs(i, j - 1) # 좌
            dfs(i, j + 1) # 우


        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == '1': # 전체노드탐색 중, 아직 방문하지 않은 땅 발견!
                    dfs(i, j) # (i,j)의 상하좌우 인접노드 모두 DFS로 방문표시완!
                    count += 1 # 방문한 섬 개수 1

        return count



solution = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
output = solution.numIslands(grid)
print(f'output :: {output}')