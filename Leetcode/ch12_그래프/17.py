# 모든 가능한 조합을 생각하니까, 완탐 중 백트래킹을 떠올릴 수 있겠지
# 그중, DFS로, 어떻게 하면 트리 구조의 그래프 형태로 나타낼 수 있을까?
# 그래프를 그려보고, dfs에 필요한 조건은? -- 주로 1. 어디까지 방문했나? 2. 현재까지 완성한 조합? 3. 방문여부?



# 문제 설명
    # 2 ~ 9까지의 숫자가 주어졌을 때, 전화번호로 가능한 모든 문자를  출력하라

# 문제 핵심
# - 각 숫자에 대응되는 알파벳이 있음 (2 -> "abc", 3 -> "def") -> dict 자료구조 사용
# - 주어진 숫자 문자열로, 만들 수 있는 모든 조합을 **완전 탐색**해야 함!
# - "트리" 구조처럼, 자리수마다 가능한 문자들을 하나씩 선택해서 조합 (트리를 그림을 그려보자!)
# - 한가지 조합(ad, ae, af..)를 끝까지 쭉 가보고, 끝에 도달하면 조합 완성! -> 결과 리스트에 저장
# - 하나의 경로가 끝나면, 다시 분기점으로 돌아가서 다른 경로 탐색 ! -> DFS의 백트래킹적 사고!!


# 자료구조, 알고리즘
# 딕셔너리 : 숫자 -> 문자 매핑
# DFS/백트래킹
    # 한 가지 조합(ad, ae, af...)을 끝까지 쭉 가보고,
    # 다시 돌아와서 다른 경로(bd, be...)를 가보는 방식.

# 시간복잡도
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        digit_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = [] # 결과 저장

        # index : 현재 몇번째 자리까지 탐색했는지, combi : 현재까지 만든 조합의 개수
        def dfs(index, combi):
            # 재귀종료조건 -> 모든 digits 자릿수를 탐색했을 때
            if index == len(digits):
                result.append(combi)
                return

            # 재귀호출부분
            start_char = digits[index]
            for value in digit_to_chars[start_char]:
                dfs(index + 1, combi + value)

        dfs(0, "")

        return result





solution = Solution()
digits = "2"
output = solution.letterCombinations(digits)
print(f'output :: {output}')