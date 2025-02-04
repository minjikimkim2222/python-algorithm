# ex1 - 제너레이터, yield, next함수 기본예제
## 아래 정의된 제너레이터 함수는, 호출될 때마다 자연수를 하나씩 생성(yield)한다
from mypy.typeops import false_only


def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n

g = get_natural_number()
## 이때, 함수 내부ㅢ 코드를 바로 생성하는 것이 아니라, 제너레이터 객체 자체를 생성하여, g라는 변수에 할당한다.
## 이제 g는, get_natural_number 제너레이터를 가리키게 된다

for _ in range(3):
    print(f"Received: {next(g)}")
    # next() 함수는, 제너레이터 객체(g)를 인자로 받아, 제너레이터가 다음으로 생성하는 값(yield)를 반환해준다

# ex2 - '여러 타입'의 값을 하나의 제너레이터에서 생성
def generator():
    yield 1
    yield 'string'
    yield False

g = generator()
for _ in range(3):
    print(f"Second Received: {next(g)}")
