# 1. print - 디버깅에 유용한 팁

## sep 파라미터로 구분자 지정
print('A1', 'B2') ## 디폴트 구분자 ' ' -> A1 B2
print('A1', 'B2', sep=',') ## A1,B2

## print 사이 줄바꿈 제거, end 파라미터를 공백으로
print('aa', end=' ')
print('bb')

## 리스트 출력 시, join으로 묶어서 출력
a = ['a', 'b']
print(a) ## ['a', 'b']
print(' '.join(a)) ## a b

## print f-string 포켓
idx = 1
fruit = "apple"
print(f"idx: {idx}, fruit: {fruit}") ## idx: 1, fruit: apple

# 2. pass
class My_Class(object):
    def method_a(self):
        pass
    def method_b(self):
        print("Method b")

c = My_Class

# 3. locals
import pprint

print("locals()호출 !! ")
pprint.pprint(locals())

## pprint는 줄바꿈 처리를 가독성 좋게 해주고, 아래는 해당 locals 사용 결과의 일부이다.
#  'a': ['a', 'b'],
#  'c': <class '__main__.My_Class'>,
#  'fruit': 'apple',
#  'idx': 1