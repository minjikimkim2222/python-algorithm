# 정렬된 nums의 짝수번째 원소의 합을 구할 것 -> 가장 파이썬 다운 풀이법
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])

solution = Solution()
nums = [6,2,6,5,1,2]
output = solution.arrayPairSum(nums)
print(f'output :: {output}')