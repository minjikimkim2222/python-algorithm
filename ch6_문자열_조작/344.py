# 문자열 뒤집기
class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

solution = Solution()
solution.reverseString(["h", "e", "l", "l", "o"])