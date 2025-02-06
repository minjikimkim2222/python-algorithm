## 정수형 -> int, bool
print(True == 1) ## True
print(False == 0) ## True

## 집합자료형 -> set
## 빈 집합
a = set()
print(a) ## set()
print(type(a)) ## <class 'set'>

## 빈 집합이 아닌, 값이 포함된 집합
a = {'a', 'b', 'c'}
print(a)

## set은 입력순서가 유지되지 않고, 중복값이 있다면 하나의 값만 유지
a = {3, 2, 3, 5}
print(a) ## {2, 3, 5}

## 가변 시퀀스, list
a = [1,2,3,4,5]
b = a

print(b)
a[2] = 4
print(a)
print(b)

# 비교연산자 is와 =의 차이
a = [1,2,3]

print(a == a) ## True
print(a == list(a)) ## True
print(a is list(a)) ## False