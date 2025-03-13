# 문제 설명
    # 1. output[i]에 자기자신을 제외한 나머지 모든 원소의 곱을 채워넣어라
    # 2. 단, 나눗셈을 하지 않고 O(n) 시간복잡도에 풀 것

# 문제 핵심
    # 시간복잡도가 O(n)이라 2중 for문을 돌릴 수 없음
    # 자기 자신을 제외한 곱셈을 쪼개서 생각해보자 -> (자기자신을 제외한 왼쪽곱) * (자기자신을 제외한 오른쪽곱)

# 사용하는 자료구조, 알고리즘
    # 오직 1중 for문
    # 배열 순회

# 시간복잡도 : O(n)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []

        # 자기자신을 제외한 왼쪽 곱을 result에 채워준다
        left = 1
        for i in range(0, len(nums)):
            result.append(left)
            left = left * nums[i]

        # 자기자신을 제외한 오른쪽 곱을 result에 채워준다 - right 곱은 배열을 거꾸로 돌며 곱해준다
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= right
            right = right * nums[i]

        return result



solution = Solution()
nums = [1,2,3,4]
output = solution.productExceptSelf(nums)
print(f'output :: {output}')
