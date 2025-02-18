# 문자열 -> 가장 긴 팰린드롬 문자열 반환
# 펠린드롬 : 문자열이 앞뒤로 대칭

class Solution:
    def longestPalindrome(self, s: str) -> str:
       ## 중심좌표를 받아, '중심좌표를 기준으로 좌우로 투포인터 확장' -> 팰린드롬 판별
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        longest_str = ""
        # 중심좌표 -> (0,0) / (1,1) / (2,2) / (3,3) / (4,4)
        for idx in range(len(s)):
            ## 홀수개의 팰린드롬
            odd_palindrome = expand_around_center(idx, idx)
            print(f'홀수개의 팰린드롬 >> 중심좌표 :: ({idx}, {idx}) // 문자열 :: {odd_palindrome}')
            if len(longest_str) < len(odd_palindrome):
                longest_str = odd_palindrome
                print(f'홀수개에서 longest 갱신 :: {longest_str}')

            ## 짝수개의 팰린드롬
            even_palindrome = expand_around_center(idx, idx + 1)
            print(f'짝수개의 팰린드롬 >> 중심좌표 :: ({idx}, {idx + 1}) // 문자열 :: {even_palindrome}')
            if len(longest_str) < len(even_palindrome):
                longest_str = even_palindrome
                print(f'짝수개에서 longest 갱신 :: {longest_str}')

        return longest_str

solution = Solution()

input_str = "babad"
ret_str = solution.longestPalindrome(input_str)
print(f'ret_str :: {ret_str}')