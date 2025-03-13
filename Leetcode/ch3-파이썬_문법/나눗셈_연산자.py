# 1. 3+ 버전, 나눗셈 연산자
print(5 / 3) ## 1.6666666666666667
print(type(5 / 3)) ## <class 'float'>

# 2. 몫 연산자
print(5 // 3) ## 1
print(type(5 // 3)) ## <class 'int'>

# 3. 나머지 연산자
print(5 % 3) ## 2
print(type(5 % 3)) ## <class 'int'>

# 4. 몫 + 나머지 동시에 구하는 함수 - divmod()
print(divmod(5, 3)) ## (1, 2)
print(type(divmod(5, 3))) ## <class 'tuple'>
