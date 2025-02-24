# 문제 설명
    # 1. output[i]에 자기자신을 제외한 나머지 모든 원소의 곱을 채워넣어라
    # 2. 단, 나눗셈을 하지 않고 O(n) 시간복잡도에 풀 것 -> 이번에는 일반적으로 풀 수 있는 풀이로 (O(n^2))

# 문제 핵심
    # 이중 for문을 돌리면서, 자기자신을 제외한 원소의 누적곱을 리스트에 append하자

# 사용하는 자료구조, 알고리즘
    # 2중 for문
    # 배열 순회

# 시간복잡도 : O(n^2)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []

        for i in nums:
            value = 1
            for j in nums:
                # 자기자신일 경우, continue
                if i == j:
                    continue
                else: # 자기자신을 제외한 원소의 누적곱
                    value = value * j
            result.append(value)


        return result


solution = Solution()
nums = [1,2,3,4]
output = solution.productExceptSelf(nums)
print(f'output :: {output}')