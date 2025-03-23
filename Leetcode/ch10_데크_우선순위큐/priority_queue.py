# heapq 모듈 설명
import heapq

pq = [] # 빈 우선순위 큐 생성

heapq.heappush(pq, 5)
heapq.heappush(pq, 1)
heapq.heappush(pq, 4)
heapq.heappush(pq, 3)
heapq.heappush(pq, 2)

print( [heapq.heappop(pq) for _ in range(len(pq))])
# 최소값 순서대로 추출 -> [1, 2, 3, 4, 5]


pq = []
heapq.heappush(pq, -5)
heapq.heappush(pq, -1)
heapq.heappush(pq, -4)
heapq.heappush(pq, -3)
heapq.heappush(pq, -2)

# print( [heapq.heappop(pq) for _ in range(len(pq))]) # [-5, -4, -3, -2, -1]
print( [-heapq.heappop(pq) for _ in range(len(pq))]) # [5, 4, 3, 2, 1]
