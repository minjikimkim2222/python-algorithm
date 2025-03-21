from collections import deque

dq = deque()
dq.append(1) # [1]
dq.append(2) # [1, 2]
dq.appendleft(3) # [3, 1, 2]

print(dq.pop()) # 2 (오른쪽 끝에서 제거) -> [3, 1]
print(dq.popleft()) # 3 (왼쪽 끝에서 제거) -> [1]