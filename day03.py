# prime number

number = int(input('number :'))
counts = 0
# k =1
# while k <= number:
#     if number % k == 0:
#         counts += 1
#     k += 1
#
# if counts == 2:
#     print(f'{number} is prime number')
# else:
#     print(f'{number} is not prime number')

for i in range(1, number + 1):
    if number % i == 0:
        counts += 1

if counts == 2:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')
