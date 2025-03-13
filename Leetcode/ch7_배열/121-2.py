# 문제 설명
    # 1. 주식을 사고 팔 때, 최대치의 이익을 반환하라
    # 2. 단, 이익이 없다면 0을 반환할 것

# 문제 핵심
    # 이익이 없다 == 배열이 내림차순
    # 성능상, for문은 1중만 돌아야함 : O(n)
        # 1. 값을 그래프로 시각화하여 나열하면, 어떤 식으로 풀어야할 지 직관이 생긴다
        # 2. 1중 for문을 돌릴 때, 기준고정! (i번째 시점은, 팔릴 때의 주식 가격)일 때,
            # 각 i번째 시점마다의 '최소' 비용을 갱신하며, 그때마다의 최대 profit을 갱신하면,
            # 최대효율의 profit을 계산할 수 있다

# 사용하는 자료구조, 알고리즘
    # 배열
    # for문 -> i번째에서의 의미 부여하며, 그 시점마다의 최소비용 / 최대이익 따로 분리해서 생각할 것 !

# 시간복잡도 : O(n)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 배열이 내림차순이면 이익이 없음
        if prices == sorted(prices, reverse = True):
            return 0
        else: # 배열 최대치 계산
            min_cost = prices[0]
            max_profit = 0
            for price in prices[1:]:
                min_cost = min(min_cost, price) # 현재 가장 싼 가격 갱신
                curr_profit = price - min_cost
                max_profit = max(max_profit, curr_profit)

            return max_profit
solution = Solution()
prices = [2,4,1]
output = solution.maxProfit(prices)
print(f'output :: {output}')