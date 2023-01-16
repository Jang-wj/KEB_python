# while
while True:
    dan = int(input('Dan? (0 to quit)'))
    if dan == 0:
        break
    if 1 < dan < 10:
        for i in range(1, 10):
            print(f'{dan} * {i} = {dan * i}')
            i = i + 1
    else:
        print('2~9 사이 숫자 입력')

