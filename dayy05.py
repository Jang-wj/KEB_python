# Function
import random


# function : prime number
def isprime(n):
    '''
    매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
    :param n: integer number
    :return: True or False
    '''
    if n <= 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    else:
        return True


help(isprime)
start = int(input('start number : '))
end = int(input('end number : '))

if start > end:
    start, end = end, start

for i in range(start, end+1):
    if isprime(i):
        print(i, end=' ')


def do_nothing():
    pass


do_nothing()
print(do_nothing())


mamamoo = ['화사', '솔라', '휘인', '문별']
print(mamamoo.pop())  # 삭제할 값 리턴 후 삭제
print(mamamoo.remove('화사'))  # 삭제만 실행, 따라서 print 함수는 None 출력


def calculate_fee(*args):
    '''
    놀이공원 요금 계산 프로그램
    :param args: age
    :return: 지불할 총 입장료
    '''
    total = 0
    for age in args:
        if 19 <= age:
            total += 10000
        else:
            total += 3000
    return total


print(calculate_fee(20, 20, 25))
print(calculate_fee(10, 7, 45, 42))


def calculate_fee(args) -> list:
    '''
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: 지불할 총 입장료, 어른 수, 아이 수, 전체 인원 수
    '''
    total = 0
    adult = 0
    child = 0
    for age in args:
        if 19 <= age:
            total += 10000
            adult += 1
        else:
            total += 3000
            child += 1
    return [len(args), adult, child, total]


nu_of_visitor = int(input('몇 분이세요?'))
ages = [random.randint(1, 60) for age in range(nu_of_visitor)]

result = calculate_fee(ages)
print(f'{result[0]}명 방문하셨고 어른 {result[1]}명, 아이 {result[2]}명, 총 요금은 {result[-1]}원 입니다.')


# return Dictionary
# def calculate_fee(args) -> dict:
#     '''
#     놀이공원 요금 계산 프로그램
#     :param args: ages in list
#     :return: {'no_of_people':지불할 총 입장료, 'no_of_adult':어른 수, 'no_of_child'아이 수, 'total_amount':전체 인원 수}
#     '''
#     total = 0
#     adult = 0
#     child = 0
#     for age in args:
#         if 19 <= age:
#             total += 10000
#             adult += 1
#         else:
#             total += 3000
#             child += 1
#     return {'no_of_people': len(args), 'no_of_adult': adult, 'no_of_child': child, 'total_amount': total}
#
#
# nu_of_visitor = int(input('몇 분이세요?'))
# ages = [random.randint(1, 60) for age in range(nu_of_visitor)]
#
# result = calculate_fee(ages)
# print(f'{result["no_of_people"]}명 방문하셨고 어른 {result["no_of_adult"]}명, 아이 {result["no_of_child"]}명, 총 요금은 {result["total_amount"]}원 입니다.')


def inha():
    """
    숫자 출력
    :return:
    """
    print(60)


def call_func(f):
    """
    매개변수로 함수를 넘겨받아 실행
    :param f: 매개변수가 함수
    :return:
    """
    f()  # 넘겨 받은 함수 실행


call_func(inha)


def substract(n1, n2):
    print(n1 - n2)


def runfunction(f, arg1, args2):
    """
    함수를 매개 변수로 받아 해당 함수를 실행
    :param f: 함수
    :param arg1: 정수 값
    :param args2: 정수 값
    :return:
    """
    f(arg1, args2)


runfunction(substract, 99, 88)


# Closures

def calculate():
    x = 1
    y = 2
    temp = 0

    def add_sub(n):
        nonlocal temp
        # x = 11  # local variable
        temp = temp + x + n - y
        return temp
    print('once')  # outer function은 한번만 실행
    return add_sub


c1 = calculate()

for i in range(5):
    print(c1(i))



# lambda

# def squares(n):
#     """
#     제곱 함수
#     :param n:
#     :return:
#     """
#     return n**2


def process(no_lists, f):
    for no in no_lists:
        print(f(no))


numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
# process(numbers, squares)
process(numbers, lambda x: x * x)


