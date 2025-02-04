# 1
a = [1,2,3,2,45,2,5]
print(a) ## [1, 2, 3, 2, 45, 2, 5]

print(enumerate(a)) ## <enumerate object at 0x102f9e100>
print(list(enumerate(a))) ## [(0, 1), (1, 2), (2, 3), (3, 2), (4, 45), (5, 2), (6, 5)]

# 2. a = ['a1', 'b2', 'c3']가 있을 때, 이 리스트의 인덱스와 값을 함께 출력하려면?
a = ['a1', 'b2', 'c3']
print(list(enumerate(a))) ## [(0, 'a1'), (1, 'b2'), (2, 'c3')]
for idx, v in list(enumerate(a)):
    print(idx, v)