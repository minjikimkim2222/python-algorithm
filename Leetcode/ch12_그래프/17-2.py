# 문제 설명 : 전화번호 조합

# 문제 핵심
    # 1. 키-값 쌍 자료형 형태 -> dict 사용
    # 2. 전화번호에 대응되는 가능한 모든 문자열의 조합 -> 완탐 -> dfs
    # 3. dfs 를 만들 때는, 트리 형태를 만들자 !!
    # 4. ** dfs(depth, discovered) **
        # 1) depth는 현재 탐색하는 깊이, discovered : 현재까지 완성한 문자열 조합
        # 2) 각 depth에서 가능한 다음 문자열이 순회하고, 그 문자를 discovered에 붙여서, 다음 depth로 "재귀호출"
        # 3) 만약 depth가 digits의 길이와 같아진다면, 한 조합이 완성되고 + 재귀 종료!
        # 3-2) 재귀가 종료되면, 그 전 브랜치로 백트래킹되고, 그다음 조합이 있는지 for문으로 또다시 순회!

# 자료구조, 알고리즘

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        digits_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        len_digits = len(digits)
        return_list = []  # 리턴할 문자열을 담을 리스트

        # depth : 현재 탐색하는 깊이, discovered: 현재까지 탐색한 문자열
        def dfs(depth, discovered):
            # 재귀 종료조건
            if depth == len_digits:
                return_list.append(discovered) # "ad"
                print(f'재귀 종료 시, :: {return_list}')
                return

            # 재귀호출부분
            start_char = digits_to_chars[digits[depth]] # "abc" / "def"

            for visit_char in start_char: # 각각 "a" "b" "c" / "d" "e" "f"
                # discovered = discovered + visit_char ** 파이썬 문자열은 immutable이라, 새롭게 변경한 문제열을 넘겨줘야함! **
                dfs(depth + 1, discovered + visit_char)




        dfs(0, "")

        return return_list




solution = Solution()
digits = "23"
output = solution.letterCombinations(digits)
print(f'output :: {output}')