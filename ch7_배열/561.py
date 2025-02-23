# 페어의 min()을 합산했을 때, max를 만들도록 하는 것
# nums = [1,4,3,2]일 때
# min( , ) + min( , ) = max가 되게끔 생각해봤더니
# 4는 1,2,3 중 누구랑 있어도 못 뽑히고
# 그러면 3은 뽑히려면 유일하게 큰 4랑 있어야 하니, (1 2) (3 4) 일 때, 최대값 sum 4가 되겠지요

# 배열이 오름차순 순서의 쌍일 때, 그때마다의 첫번째 쌍을 더한 것이 최대가 된다
class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sum = 0

        nums.sort()
        # 정렬된 배열의 0,2,.. 번째 합을 더하기
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                sum += num
        return sum

solution = Solution()
nums = [6,2,6,5,1,2]
output = solution.arrayPairSum(nums)
print(f'output :: {output}')