

graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}

# 스택을 이용한 DFS
def dfs(start_v):
    discovered = [] # 방문한 노드 리스트
    stack = [start_v] # '탐색할' 노드를 담는 스택

    while stack:
        v = stack.pop() # 스택의 맨 위(마지막 요소)에서 하나 꺼내기

        if v not in discovered:
            discovered.append(v) # 방문 처리

            for w in graph[v]: # 현재노드 v의 인접노드들을 순회
                stack.append(w) # 방문 예정인 노드를, 스택에 추가 (미리 저장)
    return discovered

output = dfs(1)
print(f'output :: {output}') # [1, 4, 3, 5, 7, 6, 2]