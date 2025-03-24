# 이 문제의 핵심
    # 1. 커서 이동이 많다! -> 중간 삽입 연산에 유리한 자료구조여야 함!!
    # 2. 커서를 기준으로 **'왼/오'**로 나눌 수 있다!
        # 커서 기준으로 왼/오를 따로 저장하면 ??
        # 배열'끝'에서 삽입/삭제 -> O(1) !!
        # 따라서 가변배열 2개 사용

# 시간에러가,, input() 함수 때문인건가?
import sys

left = list(sys.stdin.readline().rstrip())
right = []

for _ in range(0, int(sys.stdin.readline())):
    command = sys.stdin.readline().split() # 명령줄 입력
    if command[0] == 'L':
        if left:
            right.append(left.pop())

    elif command[0] == 'D':
        if right:
            left.append(right.pop())

    elif command[0] == 'B':
        if left:
            left.pop()

    else: # P $
        left.append(command[1])

print(''.join(left) + ''.join(reversed(right)))