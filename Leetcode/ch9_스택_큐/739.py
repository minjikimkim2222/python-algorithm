# 문제 설명 - '일일 온도'
    # 매일의 온도 리스트 T를 입력으로 받아서,
    # 더 따뜻한 날씨를 위해서는 며칠(i)를 기다려야 하는지, answer[i]를 반환하기
        # 만약, 더 따뜻한 날씨가 없다면, 0을 초기화할 것

# 문제 핵심
    # 우선 문제 그대로 받아들인대로, 구현했음
    # 기준값을 잡은 현재 날짜(data)와 현재 날짜 이후의 배열값들 중(compare_data), 이후의 날짜가 더 클 때 반복문 stop
    # 그때까지 wait_day count를 하고
    # flag변수를 두어서(is_exist), 더 따뜻한 날씨가 없으면 0을 append하게끔 했다

# 자료구조, 알고리즘
    # 리스트
    # Brute-force라서 비효율적이고, Timeout 에러가 났다 -> 739-2 풀이

# 시간복잡도 -> 이중 for문으로 O(n^2)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = []

        for idx, data in enumerate(temperatures):
            wait_day = 0
            is_exist = False

            for compare_data in temperatures[idx+1:]:
                if compare_data and data < compare_data:
                    wait_day += 1
                    is_exist = True
                    break
                wait_day += 1

            if is_exist:
                answer.append(wait_day)
            else:
                answer.append(0)

        return answer

solution = Solution()
tempatatures = [73,74,75,71,69,72,76,73]
output = solution.dailyTemperatures(tempatatures)
print(f'output :: {output}')