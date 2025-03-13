# 1. isdigit
print("12345".isdigit())
print("12a45".isdigit())

print("abcde".isalpha())
print("abcd2".isalpha())

# 2. split()
print("apple,banana,orange".split(','))
print("hello world".split()) ## ['hello', 'world']
print("hello world".split()[0]) ## hello

# 3. sort - 기본 오름차순/내림차순
my_list = [3, 1, 2]
my_list.sort()
my_list.sort(reverse=True)
print(my_list)

# 4. 특정 기준으로 리스트 정렬하기
my_list = ["apple", "banana432", "cherry"]

# 문자열 길이 기준으로 정렬
my_list.sort(key = lambda x : len(x))
print(my_list) ## ['apple', 'cherry', 'banana432']

# 두번째 문자 기준으로 정렬
my_list.sort(key = lambda x : x[1])
print(my_list) ## ['banana432', 'cherry', 'apple']

# 두 가지 정렬기준
arr = [("apple", 3), ("banana", 1), ("cherry", 2), ("banana", 2)]

## 첫번째 기준은 문자열 / 1을 만족하면 두번째 숫자 정렬
arr.sort(key = lambda x : (x[0], x[1]))
print(arr) ## [('apple', 3), ('banana', 1), ('banana', 2), ('cherry', 2)]