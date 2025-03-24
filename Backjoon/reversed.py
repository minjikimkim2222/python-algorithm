# 문자열, 리스트에 모두 사용가능한 reversed
# 그러나, 반환값은 문자열이나 리스트가 아닌, 반복가능한 객체(iterator)
    # 따라서, 이를 다시 list()나 str()로 감싸야 실제값을 얻을 수 있다!!

s = "hello"
reversed_s = reversed(s)
print(''.join(reversed_s)) # olleh

lst = [1, 2, 3, 4, 5]
reversed_lst = reversed(lst)
print(list(reversed_lst)) # [5, 4, 3, 2, 1]