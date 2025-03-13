# 1. 딕셔너리 선언 -> 빈 딕셔너리 선언 / 초기값 가진 딕셔너리 선언
a = dict()
a = {}

a = {'key1':'value1', 'key2':'value2', 'key3':3}
print(a) ## {'key1': 'value1', 'key2': 'value2', 'key3': 3}

# 2. 딕셔너리의 key로 value 조회
print(a['key3']) ## 3

# 3. 딕셔너리에 키/값을 삽입
a['key5'] = 7
print(a) ## {'key1': 'value1', 'key2': 'value2', 'key3': 3, 'key5': 7}

# 4. 특정 키 삭제 -> del
del a['key2']
print(a) ## {'key1': 'value1', 'key3': 3, 'key5': 7}

# 5. 딕셔너리에 키가 존재하는지 조회
if 'key1' in a:
    print('dict에 key1인 키가 존재한다.') ## dict에 key1인 키가 존재한다.
else:
    print('해당 키가 존재하지 않는다.')

# 6. 반복문으로 dict 조회
for key,value in a.items():
    print(f"key : {key}, value: {value}", end=' / ')
    ## key : key1, value: value1 / key : key3, value: 3 / key : key5, value: 7 /