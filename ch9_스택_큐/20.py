# 문제 설명 - 유효한 괄호 - ( { [   ] } )
    # 1. open 괄호는 동일한 close 괄호로 닫혀야 한다
    # 2. open 괄호는 동일한 순서로 닫혀야 한다

# 문제 핵심
    # 스택의 FIFO를 이용해야 함을 파악하기
    # 다음의 일련의 과정을 실행한다.
        # 1. 여는 괄호를 만다면 -> stack에 넣기
        # 2. 닫는 괄호를 만났는데 (예: ']')
            # 2-1) ]에 해당되는 동일한 여는 괄호([)가 스택의 top이라면, pop
            # 2-2) 동일하지 않다면 pass가 아니고!! 바로 False 리턴 (반례 : ([) - False인데 True 리턴해버림)
        # 3. 전부 다 돌고 stack에 남는 문자가 있다면 False / 없다면 True

# 자료구조, 알고리즘
    # 자료구조 - 스택의 LIFO ; 왜냐면 닫는 괄호를 만났을 때, 여는 괄호의 가장 최근 것을 비교하기 때문

# 시간복잡도

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:

            # 1. 여는 괄호를 만나면 -> stack에 넣기
            if c == '(' or c == '{' or c == '[':
                stack.append(c)

            # 2. 닫는 괄호의 종류가 stack의 top과 같다면, stack에서 pop을 한다
            else: # 종류가 다르다면 -> 바로 False를 반환해야 함 !!
                if stack and ((c == ')' and stack[-1] == '(') or
                              (c == '}' and stack[-1] == '{') or
                              (c == ']' and stack[-1] == '[') ):
                    stack.pop()
                else: # 여는 문자 대신 바로 닫는 문자 오면, False
                    return False

        # 3. stack 안에 문자열이 있는지 여부를 판단해, T/F 반환
        if stack:
            return False
        return True

solution = Solution()

s = "(])"
output = solution.isValid(s)
print(f'output :: {output}')