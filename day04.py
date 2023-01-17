# 7-1

year_list = [x for x in range(1999, 2005)]
print(year_list)

# 7-2
print('----------------------------')

print(year_list[3])

# 7-3
print('----------------------------')

print(year_list[-1])

# 7-8

surprise = ['Groucho', 'Chico', 'Harpo']

# 7-9
print('----------------------------')

surprise[-1] = surprise[-1].lower()
print(surprise[-1][::-1].title())

# 7-10

num_list = [x for x in range(10) if x % 2 == 0]
print(num_list)

# 7-11
print('----------------------------')


start1 = ['fee', 'fie', 'foe']
rhymes = [('flop', 'get a mop'),
          ('fope', 'turn the rope'),
          ('fa', 'get the cat'),
          ('fudge', 'call the judge'),
          ('fat', 'pet the cat'),
          ('fog', 'walk the dog'),
          ('fun', 'say were done')
          ]
start2 = 'Someone better'

for i in start1:
    print(f'{i.title()}!', end=' ')
print(f'{rhymes[0][0].title()}!')

for i, j in rhymes:
    print(f'{start2} {j}.')


# 8-1
print('----------------------------')
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print(e2f)

# 8-2
print('----------------------------')
print(e2f['walrus'])

# 8-3
print('----------------------------')

# f2e = {}
# for i, j in e2f.items():
#     print(i)
#     f2e[j] = i
# print(f2e)

f2e = {j: i for i, j in e2f.items()}
print(f2e)

# 8-4
print('----------------------------')

print([x for x, y in e2f.items() if y == "chien"])

# 8-5
print('----------------------------')

print(e2f.keys())

# 8-6, 8-7, 8-8, 8-9
print('----------------------------')

life = {
    'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
    'plants': '',
    'other': ''
}
print(life.keys())
print(life['animals'].keys())
print(life['animals']['cats'])

# 8-10
print('----------------------------')

squares = {x: x**2 for x in range(10)}
print(squares)

# 8-12
print('----------------------------')

print(x for x in 'Got')
for x in 'Got':
    print(x)
print(x for x in range(10))
for x in range(10):
    print(x)

# 8-13
print('----------------------------')

tup1 = ('optimist', 'pessimist', 'troll')
tup2 = ('The glass is half full', 'the glass is half empty', 'How did you get a glass?')

dic = {x: y for x, y in zip(tup1, tup2)}
print(dic)

# 8-14
print('----------------------------')
title = ['Creature of Habit', 'Crewel Fate']
plot = ['A nun turns into a monster', 'A haunted yarn shop']
movies = {x: y for x, y in zip(title, plot)}
print(movies)
