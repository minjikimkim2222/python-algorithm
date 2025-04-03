# dfs 구현 시, 스택을 이용한 반복문에서, 큐로 바꿨더니 해결된다.
# 즉, 방문가능노드후보를 저장한 자료구조에서 스택처럼 뒤(가장 최근)에서부터 뽑을지 -> pop()
# 혹은,                             큐 처럼 앞(가장 오래전)부터 뽑을지 ->  popleft() 에 따라,
# 깊이우선탐색 / 너비우선탐색이 구현된다.

graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

from collections import deque

def bfs(start_v):
    discovered = []
    queue = deque( [start_v] )

    while queue:
        v= queue.popleft() ## 핵심!! - 큐에서 가장 먼저 들어간 노드 먼저 추출

        if v not in discovered:
            discovered.append(v)

            for w in graph[v]:
                queue.append(w)

    return discovered


output = bfs(1)
print(f'output :: {output}')