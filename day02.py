import random

small = random.choice([True, False])
green = random.choice([True, False])
print(small)
print(green)
# small = True
# green = True

if small:
    if green:
        print('pea')
    else:
        print('cherry')
else:
    if green:
        print('watermelon')
    else:
        print('pumpkin')

