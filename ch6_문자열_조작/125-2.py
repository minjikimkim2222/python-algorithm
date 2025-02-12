# 1. 문자열을 풀기 쉬운 리스트로 변환 !!!!
class Solution:
    def isPalindrom(self, s: str) -> bool :
        ## 1. 전처리 -> 문자열을 리스트로 변환 (모두 소문자로 변환 + 문자,숫자 여부 검사)
        str_list = []

        for char in s:
            if char.isalnum():
                str_list.append(char.lower())

        # 2. 팰린드롬 여부 측정
        while len(str_list) > 1:
            if str_list.pop(0) != str_list.pop():
                return False
        return True

solution = Solution()
ret = solution.isPalindrom(' ')

print(ret)