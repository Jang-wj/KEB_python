# git reset 커밋 취소, git restore

# tuple
# a = 'harry',
# b = ('hatty',)
# c = ()  # empty tuple
# d = 'harry', 'ron'  # packing
# e = ('hermione')  # string
# f = ('harry', 'ron')  # packing
# g = ('hermione',)
# print(g+f)
# print(g, id(g))
# g = g+f
# print(g, id(g))
# print(g)
# print(f[1])
# x, y = f  # unpacking
# print(y)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# t1 = ('fee', 'fie', 'foe')
# t2 = ('flop',)
# t1 += t2
# print(t1)



# list

# scores = ('A+', 'B+', 'C+')
# print(scores[1])
# # scores[1] = 'C+'
# # scores[2] = 'A+'
#
# # tuple to list, list to tuple 변경 가능
#
# temp = list(scores)
# temp[1] = 'C+'
# temp[2] = 'A+'
# scores = tuple(temp)
# print(scores)

# solid 5원칙?

# bigbang = ['GD', '태양', '탑', '대성', '승리']
# exo = ['백현', '첸']
# # bigbang.append('inha')
# # bigbang.insert(1, 'inha')
# # print(bigbang)
# # exo.extend(bigbang)
# # exo = exo + bigbang
# # print(exo)
#
# exo.append(bigbang)
# print(exo)
# print(exo[2][2])
# print(exo[-1][-3])
# exo[-2] = '시우민'
# # print(exo.pop())  # 빅뱅 pop
# print(exo[2].pop())  # 승리 pop
# print(exo)
# print(exo[2].pop(-2))  # 탑 pop
# print(exo)
# del exo[2][-1]  # 대성 delete
# print(exo)
#
# exo[2].remove('GD')
# print(exo)
# exo.clear()
# print(exo)



# list sort
# primes = [2, 19, 3.0, 5, 7, 11]
# primes_sorted = sorted(primes)
# print(primes)
# print(primes_sorted)

# primes.sort()
# print(primes)

# mixed = [6, 4, 5, 'A', 7, '트와이스', 'B', 'b', '마마무']
# mixed.sort()  #error TypeError: '<' not supported between instances of 'str' and 'int'
# mixed = ['6', '4', '5', 'A', '7', '트와이스', 'B', 'b', '마마무']
# mixed.sort()  # 문자열 사전순 정렬, 숫자 먼저, 대문자 먼저
# mixed.sort(reverse=True)
# print(mixed)

# primes = [2, 19, 3.0, 5, 7, 11]
# primes_cp = primes
# print(primes)
# print(primes_cp)
# primes[-1] = 'lunch time'
# print(primes)
# print(primes_cp)

# a = [1, 2, 3]
# b = a.copy()
# c = list(a)
# d = a[:]
# a[2] = 'sw'  # immutable
# print(a, b, c, d)

# a = [1, 2, [5, 9]]
# b = a.copy()
# c = list(a)
# d = a[:]
# a[2][1] = 7  # mutable, b,c,d affect
# print(a, b, c, d)

# import copy
# a = [1, 2, [5, 9]]
# b = copy.deepcopy(a)
# a[2][1] = 7  # mutable, deepcopy
# print(a, b)


# list comprehension
# number_list = list(range(1, 6))
# number_list2 = [num for num in range(1, 6)]
# number_list3 = [num-1 for num in range(1, 6)]
# number_list4 = [num for num in range(1, 6) if num % 2 == 1]
# odd_lists = []
# for i in range(1, 11):
#     if i % 2 == 1:
#         odd_lists.append(i)
# odd_lists = [i for i in range(1,11) if i % 2 == 1]
# odd_tuples = (i for i in range(1,11) if i % 2 == 1)  # tuple comprehension은 없음 generator = 메모리 공간 사용x 발생 후 사라짐
# print(odd_tuples)


# 7-4, 7-5, 7-6, 7-7 연습문제
# things = ['mozzarella', 'cinderella', 'salmonella']
# things[1] = things[1].title()
# print(things)
# things[0] = things[0].upper()
# print(things)
# print(f'Delete {things.pop()}')
# print(things)
# for things in things:
#     print(things.title())




