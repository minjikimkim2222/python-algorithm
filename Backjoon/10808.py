# 배운 점 - 문자열 입력받는 함수, print의 end 옵션
words = input()
ret_arr = [0] * 26

for word in words:
    int_word = ord(word) # 각 문자에 대응되는 아스키코드로 변환
    ret_arr[int_word - 97] += 1

for ret in ret_arr:
    print(ret, end=' ')

