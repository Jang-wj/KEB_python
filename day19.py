def notation(base, n):
    if n < base:
        print(number_char[n], end=' ')
    else:
        notation(base, n // base)
        print(number_char[n % base], end=' ')


number_char = [x for x in range(10)]
number_char += [chr(65 + x) for x in range(6)]

number = int(input('10진수 입력:'))
print('2진수 : ', end=' ')
notation(2, number)
print('\n8진수 : ', end=' ')
notation(8, number)
print('\n16진수 : ', end=' ')
notation(16, number)
