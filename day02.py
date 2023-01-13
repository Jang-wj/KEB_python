import random

limits = 20
tweets = 'home' * random.randint(1, 10)
diff = limits - len(tweets)
# if diff := limits - len(tweets) >= 0 :
if diff >= 0 :
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)}초과')

