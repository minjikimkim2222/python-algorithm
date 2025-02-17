# 가장 흔한 단어
# -> banned에 해당하지 않되, 가장 많이 언급된 단어를 리턴하라
# -> paragraph는 대소문자를 구분하지 않으며 + 답은 소문자를 리턴한다

import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        # 문자열 전처리 - 각 단어의 구두점 제거 + 모두 소문자
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        # collections.Counter로 리스트의 최다빈도수의 단어 리턴
        max_count_words = collections.Counter(words)
        return max_count_words.most_common(1)[0][0]

solution = Solution()
paragraph = "Bob hit a ball! the hit BALL flew far after it was hit!"
banned = ["hit"]

output = solution.mostCommonWord(paragraph, banned)
print(f"output :: {output}")