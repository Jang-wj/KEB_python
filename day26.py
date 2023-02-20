import random


def bin_search(ary, f_data):
    start = 0
    end = len(ary) - 1

    while start <= end:
        mid = (start + end) // 2
        if f_data == ary[mid]:
            return mid
        elif f_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_array = [random.choice(data_array) for _ in range(20)]

print('#오늘 판매된 전체 물건(중복O, 정렬X) -->', sell_array)
sell_array.sort()
print('#오늘 판매된 전체 물건(중복O, 정렬O) -->', sell_array)
sellProduct = list(set(sell_array))
print('#오늘 판매된 물품 종류(중복x) -->', sellProduct)

countList = []
for product in sellProduct:
    count = 0
    pos = 0
    while pos != -1:
        pos = bin_search(sell_array, product)
        if pos != -1:
            count += 1
            del (sell_array[pos])
    countList.append((product, count))

print("결산 결과 ==>", countList)
print()


def seq_search(ary, f_data):
    global count
    position = -1
    for i in range(len(ary)):
        count += 1
        if ary[i] == f_data:
            position = i
            break
    return position


def binary_search(ary, f_data):
    global count
    start = 0
    end = len(ary) - 1

    while start <= end:
        count += 1
        mid = (start + end) // 2
        if f_data == ary[mid]:
            return mid
        elif f_data > ary[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1


data_ary, sorted_ary = [], []
fin_data = 7878
count = 0

data_ary = [random.randint(0, 999999) for _ in range(1000000)]
data_ary.insert(random.randint(0, 1000000), fin_data)
sorted_ary = sorted(data_ary)

print('#비정렬 배열(100만개) -->', data_ary[0:5], '~~~~', data_ary[-5:len(data_ary)])
print('#정렬 배열(100만개) -->', sorted_ary[0:5], '~~~~', sorted_ary[-5:len(sorted_ary)])

count = 0
pos = seq_search(data_ary, fin_data)
if pos != -1:
    print('순차 검색(비정렬 데이터) -->', count, '회')

count = 0
pos = binary_search(sorted_ary, fin_data)
if pos != -1:
    print('이진 검색(정렬 데이터) -->', count, '회')
