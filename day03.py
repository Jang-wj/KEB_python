# 5-4

letter = '''Dear {0} {1}, Thank you for your letter. We are sorry that our {2} {3} in your {4}. Please note that it should never be used in a {4}, especially near any {5}. 
Send us your receipt and {6} for shipping and handling. We will send you another {2} that, in our tests, is {7}% less likely to have {3}
Thank you for you support. 
Sincerely,
{8}
{9}'''

# 5-5
salutation = 'salute'
name = 'Kim'
product = 'phone'
verbed = 'crashed'
room = 'class'
animal = 'cat'
amount = 100
percent = 90
spokeman = 'Kang'
job_title = 'teammate'

print(letter.format(salutation, name, product, verbed, room, animal, amount, percent, spokeman, job_title))


# 5-6
nameduck = 'duck'
namegourd = 'gourd'
namespitz = 'spitz'
print('-----------------------')
print('%sy Mc%sface' % (nameduck.capitalize(), nameduck.capitalize()))
print('%sy Mc%sface' % (namegourd.capitalize(), namegourd.capitalize()))
print('%sy Mc%sface' % (namespitz.capitalize(), namespitz.capitalize()))


# 5-7
print('-----------------------')
print('{0}y Mc{0}face'.format(nameduck.capitalize()))
print('{0}y Mc{0}face'.format(namegourd.capitalize()))
print('{0}y Mc{0}face'.format(namespitz.capitalize()))


# 5-8
print('-----------------------')
print(f'{nameduck.capitalize()}y Mc{nameduck.capitalize()}face')
print(f'{namegourd.capitalize()}y Mc{namegourd.capitalize()}face')
print(f'{namespitz.capitalize()}y Mc{namespitz.capitalize()}face')



# 6-2
print('-----------------------')
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('too low')
    elif number > guess_me:
        print('oops')
    else:
        print('found it')
        break
    number += 1


# 6-3
print('-----------------------')

guess_me = 5

for number in range(10):
    if number < guess_me:
        print('too low')
    elif number > guess_me:
        print('oops')
    else:
        print('found it')

