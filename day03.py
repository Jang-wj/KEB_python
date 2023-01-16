# input 2 number

# start = int(input('start number : '))
# end = int(input('end number : '))
# print(start, end)


# start_end = input('start and end number : ').split()
# print(int(start_end[0]), int(start_end[1]))

start = int(input('start number : '))
end = int(input('end number : '))

if start > end:
    start, end = end, start

for i in range(start, end+1):
    if i <= 1:
        continue
    for k in range(2, i):
        if i % k == 0:
            break
    else:
        print(i, end=' ')
