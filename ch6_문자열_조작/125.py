# 1. 모든 대문자 -> 소문자
# 2. 알파벳이 아닌 문자,숫자는 삭제
# 3. 앞뒤로 읽는 문자가 같음
from operator import truediv

## 문제 첫번째 시도 - 직관적으로 비교
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_remove_not_alnum = ""

        for s_char in s:
            if s_char.isalnum():
               s_remove_not_alnum += (s_char)
            else:
                continue

        s_to_upper = s_remove_not_alnum.upper()

        print(s_to_upper)

        mid_index = len(s_to_upper) // 2
        str_len = len(s_to_upper) - 1

        for idx, s_char in enumerate(s_to_upper[:mid_index]):
            if s_char != s_to_upper[str_len - idx]:
                return False

        return True



solution = Solution()
ret = solution.isPalindrome(" ")
print(ret)
