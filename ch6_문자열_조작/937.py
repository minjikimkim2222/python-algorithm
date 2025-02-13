class Solution:
    def reorderLogFiles(self, logs : list[str]) -> list[str]:
        # 문자와 숫자 로그를 분리
        digits = []
        letters = []

        for log in logs:
            if log.split()[1].isalpha():
                letters.append(log)
            else:
                digits.append(log)

        print(f"digits :: {digits}")
        print(f"letters :: {letters}")

        # letters 리스트 정렬 (1. 두번째 문자열 ~ 끝 문자열까지 오름차순 / 2. 첫번째 문자열 오름차순)
        letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))

        # digits 각 문자열을, letters 리스트에 붙이기
        for digit in digits:
            letters.append(digit)

        return letters

solution = Solution()
ret = solution.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"])
print(ret)