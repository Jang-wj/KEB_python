# Generator
# 시퀀스를 생성하는 객체, 메모리에 생성하고 정렬할 필요없이 순회(iterate)할 수 있다
# 제네레이터는 마지막 호출을 기억하고 이전 호출은 메모리가 없음

# yield
# 함수를 제너레이터로 만듦, 함수에서 yield가 리턴을 대신함,
def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


def a():  # yield는 리턴해주지만 함수가 중단되지 않음
    yield 1
    yield 2
    yield 3


def b():  # return은 1만
    return 1  # stop
    return 2
    return 3


print(a(), b())
for i in a():
    print(i)

c = a()
print(c)
for i in c:
    print(i)

# decorator
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b


print(add_ints(3, 5))
cooler_add_ints = document_it(add_ints)
print(cooler_add_ints(3, 5))


@document_it
def sub_int(x, y):
    return x - y


print(sub_int(7, 3))


def change_print_global():
    global g
    print(g)
    g = 2  # 지역 변수
    print(g)


g = 1  # 전역 변수

print(g)
change_print_global()


# 재귀 함수 Recursion
def factorial_iter(n):
    """
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: integer 팩토리얼 결과 값
    """
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result


print(factorial_iter(5))

def factorial_recu(n):
    """
    재귀 함수를 사용한 팩토리얼 계산 함수
    :param n: n
    :return: 자기 자신을 호출 or 1
    """
    if n == 1:  # 끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n


print(factorial_recu(5))


# 예외
def div_calc(a, b):
    """
    나누기 함수
    :param a: 분자
    :param b: 분모
    :return: 계산결과
    """
    return a/b


print(div_calc(15, 3))
# print(div_calc(15, 0))

# try:
#     expr = input('분자 분모 입력:').split()
#     print(int(expr[0])/int(expr[1]))
# except:
#     print('분모에 0이 올 수 없습니다.')

# 다중 except
# try:
#     # raise Exception('쉬는 시간')  # raise 예외를 만들기, java throw
#     # raise TypeError('타입에러')
#     # raise ValueError('밸류에러')
#     expr = input('분자 분모 입력:').split()
#     print(int(expr[0])/int(expr[1]))
# except ValueError as err:
#     print(f'숫자를 입력하세요. {err}')
# except ZeroDivisionError as err:
#     print(f'분모에 0이 올 수 없습니다. {err}')
# except IndexError as err:
#     print(f'입력 값의 범위에 문제가 있습니다. {err}')
# except Exception as other:
#     print(f'예외 발생! {other}')
# else:  # 예외가 발생하지 않았을 때 실행
#     print('프로그램 정상', end=' ')
# finally:  # 예외 발생여부와 관계없이 무조건 실행
#     print('종료')


# 연습문제
# 9-1
def good():
    return ['Harry', 'Ron', 'Hermione']

# 9-2
def get_odds():
    for i in range(10):
        if i % 2:
            yield i


cnt = 1
for i in get_odds():
    if cnt == 3:
        print(i)
    cnt += 1

