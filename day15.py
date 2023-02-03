def find_and_insert_data(friend, k_count):  # idx
    findPos = -1
    for i in range(len(katok[1])):
        pair = katok[1][i]
        if k_count >= pair:
            findPos = i
            break
    if findPos == -1:
        findPos = len(katok[1])

    insert_data(findPos, friend, k_count)


def insert_data(position, friend, k_count):
    if position < 0 or position > len(katok[1]):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    for i in range(len(katok)):
        katok[i].append(None)  # 빈 칸 추가

    for i in range(len(katok)):
        for k in range(len(katok[1]) - 1, position, -1):
            katok[i][k] = katok[i][k - 1]
            katok[i][k - 1] = None

    katok[0][position] = friend
    katok[1][position] = k_count


# katok = [('다현', 200), ('정연', 150), ('쯔위', 90), ('사나', 30), ('지효', 15)]
katok = [['다현', '정연', '쯔위', '사나', '지효'], [200, 150, 90, 30, 15]]

if __name__ == "__main__":
    # while True:
        data = input("추가할 친구--> ")
        count = int(input("카톡 횟수--> "))
        find_and_insert_data(data, count)
        print(katok)
