import random

secret = random.randint(1, 10)
while True:
    guess = int(input())
    if secret > guess :
        print('too low')
    elif secret < guess :
        print('too high')
    elif secret == guess:
        print('just right')
        break
