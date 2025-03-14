# 문제 설명 - '일일 온도'
    # 매일의 온도 리스트 T를 입력으로 받아서,
    # 더 따뜻한 날씨를 위해서는 며칠(i)를 기다려야 하는지, answer[i]를 반환하기
        # 만약, 더 따뜻한 날씨가 없다면, 0을 초기화할 것

# 문제 핵심
    # 과거의 온도값들 (한개, 여러개..) 을 따로 잘 저장하고, 현재 온도값과 비교한다 (더 따뜻한 온도가 나올 때까지)
    # 과거의 온도값들을 잘 저장할 자료구조가 필요하다
    # 이때, 나는 각 날짜를 순서대로 살피고 + 저장한 과거온도값들 중, 가장 최근값과 현재 온도를 비교해, 값 갱신 필요!


# 자료구조, 알고리즘
    # 자료구조 - 스택


# 시간복잡도 -> O(n)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        # 정답 배열 초기화
        answer = [0] * len(temperatures)
        stack = []

        # 현재 온도
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_idx = stack.pop()
                answer[prev_idx] = i - prev_idx
            stack.append(i)

        return answer

solution = Solution()
tempatatures = [73,74,75,71,69,72,76,73]
output = solution.dailyTemperatures(tempatatures)
print(f'output :: {output}')