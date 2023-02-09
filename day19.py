def add_number(n):
    if n<=10:
        return 10
    return n + add_number(n-1)


print(add_number(100))


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


print(factorial(5))


def print_star(n):
    if n>=1:
        print('*' * n)
        print_star(n-1)


print_star(5)


import random


def ary_sum(arr, n):
    """
    배열 안에 들어있는 값의 합을 재귀로 구하는 함수
    :param arr: 합 할 배열
    :param n: 배열의 인덱스
    :return: 배열의 합
    """
    if n <= 0:
        return arr[0]
    return arr[n] + ary_sum(arr, n-1)


ary = [random.randint(1, 1000) for _ in range(random.randint(10, 20))]
print(ary)
print(f'배열 합계 = {ary_sum(ary, len(ary)-1)}')


def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


print('피보나치 수 = 0 1', end=' ')
for i in range(2, 10):
    print(fibo(i), end=' ')
