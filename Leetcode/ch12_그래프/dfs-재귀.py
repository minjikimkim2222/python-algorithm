# 재귀를 이용한 dfs 구현

graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

def dfs(v, discovered = []):
    # 1. 현재 정점 방문 기록 (중복 방문 방지)
    discovered.append(v)

    # 2. 재귀호출을 통해, '아직 방문하지 않은, 현재 노드 기준 인접노드' 먼저 탐색한다
    for w in graph[v]:
        if w not in discovered:
            discovered = dfs(w, discovered)

    return discovered

output = dfs(1)
print(f'output :: {output}') ## [1, 2, 5, 6, 7, 3, 4]