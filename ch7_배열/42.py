# Trapping Rain Water

# 높이를 입력받아, 비 온 후 얼마나 많은 물을 가둘 수 있는지 계산하라

# 문풀 - 투포인터
# 문제의 핵심은 '높이'고, 어떤 것을 기준으로 left, right를 가를까 했는데
# 문제상 가둘 수 있는 물의 높이를 판단할 때, max-height 기준(3)으로 나누어도 되었음

# 문제의 핵심은 '높이'를 기준으로 아래 상황을 생각해봄
# 그림상 가장 높이가 높인 것을 기점으로 왼쪽'끝'과 오른쪽'끝'에서부터 각각 중심을 향해 나아가며,
# 가둘 수 있는 물의 개수를 생각해봄 !!

# 관찰 결과 !!
# left_max는 일단 가장 왼쪽 끝으로 초기화한다
# 현재 배열이 읽는 left의 높이가 left_max보다 크다면(높다면) -> max_height 갱신
# 현재 배열이 읽는 left의 높이가 left_max보다 작다면 -> (max_height - 현재 높이)만큼 volume 더하기


class Solution:
    def trap(self, height: list[int]) -> int:
        left_idx, right_idx = 0, len(height) - 1
        left_max, right_max = height[left_idx], height[right_idx]
        water_count = 0

        while left_idx < right_idx: # 두 포인터가 만나기 전까지! (만나면, 배열의 모든 원소를 각각 탐색한 것임)
            # 매번 max height 값 갱신
            left_max = max(left_max, height[left_idx])
            right_max = max(right_max, height[right_idx])

            # 더 낮은 높이를 기준으로 포인터 이동 -> water_count는 더 낮은 높이를 기준으로 채우는 것이기에
            if left_max <= right_max: # 왼쪽 포인터가 더 작음 -> 왼쪽 높이 계산
                water_count += (left_max - height[left_idx])
                left_idx += 1
            else: # 오른쪽 포인터 높이가 더 작음 -> 오른쪽 포인터 계산
                water_count += (right_max - height[right_idx])
                right_idx -= 1

        return water_count




solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
output = solution.trap(height)
print(f'output :: {output}')