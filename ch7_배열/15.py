# 3Sum

# 세수의 합을 브루트포스로 풀면, O(n^3)이니 -- 두번째 풀이 먼저 해보고, 1번 풀이도 해볼 것
# 두 조합을 먼저 고른 뒤 -> 합을 0으로 만드는 나머지 1개가. 앞선 2개 조합을 제외하고 존재하는지 체크

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        nums.sort()
        for i in range(0, len(nums) - 2): # 세수의 조합 중 i는 len(nums) - 2까지 해야, 다른 j,k를 nums에서 차지할 수 있다
            if i > 0 and nums[i] == nums[i - 1]:  # i 기준, 중복된다면 continue
                continue

            left_idx, right_idx = i + 1, len(nums) - 1 # 두 포인터 초기화

            while left_idx < right_idx:
                total_sum = nums[i] + nums[left_idx] + nums[right_idx]

                if total_sum == 0: # 세 수의 합이 0이면
                    result.append([nums[i], nums[left_idx], nums[right_idx]])
                    print(f'세수의 합 : 0 / i : {i} / left : {left_idx} / right : {right_idx}')

                    # 중복 값 건너뛰기 - list에 값을 넣은 후, 그다음 left 중복 여부 체크
                    while left_idx < right_idx and nums[left_idx] == nums[left_idx + 1]:
                        left_idx += 1 # 미리 left 건너뛰기
                        print(f'중복값 건너뛴 후, left : {left_idx}')

                    while left_idx < right_idx and nums[right_idx] == nums[right_idx - 1]:
                        right_idx -= 1 # 미리 right 건너뛰기
                        print(f'중복값 건너뛴 후, right : {right_idx}')

                    # 만족했다면, 그다음 경우의 수 찾기
                    left_idx += 1
                    right_idx -= 1
                elif total_sum < 0:
                    left_idx += 1
                else:
                    right_idx -= 1

        return result

solution = Solution()

nums = [-2, 0, 0, 2, 2]
output = solution.threeSum(nums)
print(f'output :: {output}')