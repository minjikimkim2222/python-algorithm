# Two Sum

# 정수 배열 nums 중 2개의 원소의 합이 => target이 일치하는 순간의 인덱스 배열을 리턴할 것

# 풀이법1. 이중 for문으로 전체 순회 - 브루트 포스

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

solution = Solution()

input_arr = [3,3]
target = 6
ret_arr = solution.twoSum(input_arr, target)
print(f'ret_arr : {ret_arr}')