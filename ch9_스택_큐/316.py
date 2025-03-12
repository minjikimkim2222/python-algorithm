# 문제 설명
    # 1. 모든 문자는 한번만
    # 2. 문자열 출현 순서 유지하되, 가능한 사전순 최소(==문자열 오름차순)

# 문제 핵심 풀이
    # 새로운 문자가 기존 문자보다 작고, 기존문자의 남은 개수가 뒤에 존재한다면, 쌓아둔 걸 꺼내서 없앤다.
# 자료구조, 알고리즘
    # '나온 빈도수 세기' -> Collections.Counter
    # '중복 제거' -> Set
    # 그렇다면 '스택'을 떠올린 사고과정 -> '제거' 기준 생각..
        # 1) '새로운 문자'가 '기존 문자'보다 더 작고, '기존문자'가 뒤에 존재한다면?
        #      -> 기존 문자 제거 & 새로운 문제 넣기!
        # 2) 이과정이 되려면, '가장 최근에 넣은 걸, 먼저 빼야 함' -> FIFO -> Stack

# 시간복잡도 :


from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = [] # 최종 스택에 넣을 값
        in_stack_without_duplicate = set() # stack 안 문자열 중복 체크

        for char in s:
            # 현재 Counter 개수 1개 빼기
            counter[char] -= 1

            # 이미 스택 안에 해당 문자열이 존재하는지 중복 체크
            if char in in_stack_without_duplicate:
                continue

            # 새로운 문자가 기존문자보다 작고, 새로운 문자가 뒤에도 존재(==중복 count > 0)하면
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                removed_data = stack.pop()
                in_stack_without_duplicate.remove(removed_data)


            # 중복이 아닌 문자는 항상 넣음
            stack.append(char)
            in_stack_without_duplicate.add(char)

        return "".join(stack)


solution = Solution()
s1 = "bcabc"
s2 = "cbacdcbc"
output = solution.removeDuplicateLetters(s1)
print(f'output :: {output}')
