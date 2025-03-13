# 풀이법3. 자료형을 dict로 바꿔서, target - n을 딕셔너리의 키로 조회
# 딕셔너리의 키 => '조회조건'

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict_arr = dict()

        # key에 원소의 값, value에 해당 원소의 인덱스로, 딕셔너리 저장
        for idx, n in enumerate(nums):
            dict_arr[n] = idx

        # 첫번째 원소를 제외한 나머지 배열이 dict의 키에 존재하는지 조회
        for i in nums:
            key = target - i
            if key in dict_arr and nums.index(i) != dict_arr[key]:
                return [nums.index(i), dict_arr[key]]



solution = Solution()
input_arr = [3,3]
target = 6
ret_arr = solution.twoSum(input_arr, target)
print(f'ret_arr : {ret_arr}')