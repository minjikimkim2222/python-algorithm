# List-Comprehension

# 1. 리스트 컴프리헨션 예시
## 홀수인 경우, 2를 곱해 출력하라는 리스트 컴프리헨션
a = [n * 2 for n in range(1, 10+1) if n % 2 == 1]
print(a) ## [2, 6, 10, 14, 18]

## 만약 리스트 컴프리헨션을 쓰지 못한다면..
a2 = []
for n2 in range(1, 10+1):
    if n2 % 2 == 1:
        a2.append(n2 * 2)
print(a2)

# 2. 리스트 외의 딕셔너리도 리스트 컴프리헨션 적용이 가능하다
## 리스트 컴프리헨션이라고, 리스트만 가능한 것도 아니다
## 리스트 외에도 다음과 같은 딕셔너리도 가능하다

## 리스트 컴프리헨션 전, 딕셔너리
original = {"a": 1, "b": 2, "c": 33}
a = {}
for key,value in original.items():
    a[key] = value
print(a) ## {'a': 1, 'b': 2, 'c': 33}

## 리스트 컴프리헨션 적용
b = {key: value for key,value in original.items()}
print(b)