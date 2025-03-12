# 20.py와 풀이법이 거의 동일하지만,
# {는 }처럼 짝이 정해져 있으니,아래처럼 dict() 사용 !


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        # 유효한 문자 검사
        for char in s:
            if char in mapping: # 문자 char이 mapping의 키와 동일하다면 == 여는 괄호에 해당되면..
                stack.append(char)
            else: # 닫는 괄호라면.. -> stack이 빈 상태(닫는 괄호 앞에 여는 괄호가 없음)
                if not stack or char != mapping[stack.pop()]:
                    return False

        return len(stack) == 0

solution = Solution()
s = "(){}("
output = solution.isValid(s)
print(f'output :: {output}')