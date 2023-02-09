import random


def find_min_idx(ary):
    min_idx = 0
    for i in range(1, len(ary)):
        if ary[min_idx] > ary[i]:
            min_idx = i
    return min_idx


def find_insert_idx(ary, data):
    find_idx = -1
    for i in range(0, len(ary)):
        if ary[i] > data:
            find_idx = i
            break
    if find_idx == -1:
        return len(ary)
    else:
        return find_idx


def quick_sort(ary):
    global cnt
    n = len(ary)
    if n <= 1:
        return ary

    pivot = ary[n//2]
    left_ary, mid_ary, right_ary = [], [], []

    for num in ary:
        if num < pivot:
            left_ary.append(num)
        elif num > pivot:
            right_ary.append(num)
        else:
            mid_ary.append(num)
        cnt += 1

    return quick_sort(left_ary) + mid_ary + quick_sort(right_ary)


cnt = 0
data_ary = [random.randint(1, 100) for _ in range(10)]

print(data_ary)
data_ary = quick_sort(data_ary)
print(data_ary)
print(cnt)
