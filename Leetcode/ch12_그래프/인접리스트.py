# 파이썬의 딕셔너리로 인접리스트 표현
    # key : 출발노드
    # value : 도착노드
graph = {
    1 : [2, 3, 4],
    2 : [5],
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3]
}