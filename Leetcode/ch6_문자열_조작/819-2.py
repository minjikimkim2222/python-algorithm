# 819에서 쓰인 문법 정리

## 1. 리스트 컴프리헨션 - 한 줄의 코드로 리스트를 만들어 반환해줌
# 1 ~ 10까지의 제곱 리스트 만들기
squares = [x ** 2 for x in range(1, 11)]
print(squares)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 1 ~ 10까지 짝수만 필터링
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
# [2, 4, 6, 8, 10]

# 대문자로 변환
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print(upper_words)
# ['APPLE', 'BANANA', 'CHERRY']

## 2. 정규식 (Regular Expressions, re 모듈)
# 정규식은, 문자열에서 특정 패턴을 찾거나 / 바꾸거나 / 추출하는데 사용됨
import re

text = "Hello!!! How are you???"
# * 특수 문자 제거 *
clean_text = re.sub(r'[^\w]', '', text)
print(clean_text)
## HelloHowareyou

clean_text2 = re.sub(r'[^\w]', ' ', text)
print(clean_text2)
## Hello    How are you

clean_text3 = re.sub(r'[^\w\s]', '', text)
print(clean_text3)
## Hello How are you

## 3. collections.Counter
import collections

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = collections.Counter(fruits)
most_common = counter.most_common(1)

print(counter)
## Counter({'apple': 3, 'banana': 2, 'orange': 1})
print(most_common)
## [('apple', 3)]
