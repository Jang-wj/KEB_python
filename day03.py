# prime number

number = int(input('number : '))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break
    print(i)


if is_prime:
    print(f'{number} is prime number')
else:
    print(f'{number} is not prime number')

