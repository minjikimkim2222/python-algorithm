# 가장 흔한 단어
# -> banned에 해당하지 않되, 가장 많이 언급된 단어를 리턴하라
# -> paragraph는 대소문자를 구분하지 않으며 + 답은 소문자를 리턴한다

import re
import collections

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # 문자열 전처리 - 특수문자 제거, 소문자
        except_punct_list = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                             .lower().split()
                             if word not in banned]

        # collections.Counter()로 리스트의 개수 반환
        list_count = collections.Counter(except_punct_list)
        return list_count.most_common(1)[0][0]

solution = Solution()
paragraph = "a, a, a, a, b,b,b,c, c"
banned = ["a"]

output = solution.mostCommonWord(paragraph, banned)
print(f"output :: {output}")