# sorted, join

word = 'eat'
sorted_word = sorted(word)
print(sorted_word) # ['a', 'e', 't']

sorted_word_joined1 = '_'.join(sorted_word)
print(sorted_word_joined1) # a_e_t

sorted_word_joined2 = ''.join(sorted_word)
print(sorted_word_joined2) # aet

sorted_word_joined3 = "()".join(sorted_word)
print(sorted_word_joined3) # a()e()t

# dict() 자료형은 언제 쓰는지
# {(키1,값1), (키2,값2) .. } -> 각 '키'별로 어떤 '값'들이 있는지 구분할 때..

# 학생들의 점수를 저장하는 딕셔너리
scores = {
    'Alice' : 75,
    'Bob': 92,
    'Charlie': 78
}

print(scores['Bob']) # 92

for key, value in scores.items():
    print(f'key : {key}, value : {value}')

# key : Alice, value : 75
# key : Bob, value : 92
# key : Charlie, value : 78

lst = [3,1,2]
lst.sort()
print(lst)
lst.sort(reverse = True)
print(lst)

lst = [3,1,2]
print(sorted(lst))
print(sorted(lst, reverse=True))