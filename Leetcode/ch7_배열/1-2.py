# 풀이법2. in을 이용한 탐색

# 모든 조합을 탐색하는 대신, 탐색 범위를 좁혀본다
# 첫번째 for문에서, target - n의 원소가 배열의 [idx + 1:] 범위에 존재하는지 탐색
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx, n in enumerate(nums):

            complement = target - n
            if complement in nums[idx + 1:]: # 범위 내의 complement가 있는지 체크
                return [idx, nums[idx + 1:].index(complement) + (idx + 1)]

solution = Solution()
input_arr = [3,3]
target = 6
ret_arr = solution.twoSum(input_arr, target)
print(f'ret_arr : {ret_arr}')