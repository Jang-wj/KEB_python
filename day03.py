univ = 'Inha University'

print(univ[5:])
print(univ[5:15])  # end-1
print(univ[-10:])
print(univ[::2])
print(univ[5:-6])
print(univ[-10:-6])

print(len(univ))
print(univ.split())  # delimiter

pokemons_list = ['피카츄', '꼬부기', '파이리', '이상해']
pokemons_string = ' / '.join(pokemons_list)
print(pokemons_string)

inha = 'a duck goes into a bar'
print(inha.replace('a ', 'a nice '))

subject = ' $ python, data structure, database $$$'
print(subject.strip('$'))

print(subject.find('data'), subject.index('data'))
print(subject.find('inha'))  # -1 return
# print(subject.index('inha'))   # exception
print(subject.rfind('data'), subject.rindex('data'))
print(subject.count('data'))

# 5-1 연습문제
song = '''When an eel grabs your arm, And it causes great harm, That's a moray'''
song_list = song.split()
if 'moray' in song_list:
    song_list[-1] = song_list[-1].title()
    song_string = ' '.join(song_list)
    print(song_string)



