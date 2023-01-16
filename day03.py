# prime number

number = int(input('number :'))
counts = 0

for i in range(2, number):
    if number % i == 0:
        counts += 1

if counts:
    print(f'{number} is not prime number')
else:
    print(f'{number} is prime number')
