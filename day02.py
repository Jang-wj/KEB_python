# Chapter 4

a = []
print(bool(a))
a.append(5)
print(bool(a))
print(bool(set()))
print(bool(dict()))
print(bool(''))
print(bool('aaa'))

letter = 'o'
vowels = 'aeiou'
if letter in vowels:
    print('실행')

limits = 20
tweets = 'home' * 6
diff = limits - len(tweets)
# if diff := limits - len(tweets) >= 0 :
if diff >= 0 :
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)}초과')

