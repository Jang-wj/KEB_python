# 연습 문제 9-3

def test(func):
    def inner(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return inner


def hi():
    print('hi')


decorate_hi = test(hi)
decorate_hi()


@test
def deco_hi():
    print('deco hi')


deco_hi()


# 9-4

class OopsException(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise OopsException()
    print(nick)


try:
    say_nick('바보')
except OopsException:
    print('Caught an oops')



