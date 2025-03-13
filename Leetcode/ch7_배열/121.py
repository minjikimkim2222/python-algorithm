# 문제 설명
    # 1. 주식을 사고 팔 때, 최대치의 이익을 반환하라
    # 2. 단, 이익이 없다면 0을 반환할 것
# 문제 핵심
    # 이익이 없다 == 배열이 내림차순
    # 이익이 있되, 최대치 이익 반환 == min값에 사고 max에 팔기

# 사용하는 자료구조, 알고리즘
    # 배열
    # min, max

# 시간복잡도 : O(n^2) -> time out

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 배열이 내림차순이면 이익이 없음
        if prices == sorted(prices, reverse = True):
            return 0
        else: # 배열 최대치 계산
            profit = 0
            for i in range(0, len(prices) - 1): # 배열의 마지막 인덱스가 min이 되면 안됨
                for j in range(i+1, len(prices)):
                    if prices[j] > prices[i] and (prices[j] - prices[i] > profit):
                        profit = prices[j] - prices[i]

            return profit


solution = Solution()
prices = [2,4,1]
output = solution.maxProfit(prices)
print(f'output :: {output}')