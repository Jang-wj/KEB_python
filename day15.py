def insert_data(idx, pokemon):
    """
    선형리스트에 값을 중간에 삽입
    :param idx:
    :param pokemon:
    :return:
    """
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons)-1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가

def delete_data(idx):
    """
    선형 리스트에 idx값 뒤의 값들을 제거
    :param idx:
    :return:
    """
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return

    for _ in range(len(pokemons) - idx):
        pokemons.pop()
    # for i in range(idx + 1, len(pokemons)):
    #     pokemons[i] = None
    #
    # for i in range(idx, len(pokemons)):
    #     pokemons.pop()

    # del pokemons[idx:]

def add_data(pokemon):
    """
    선형 리스트에 pokemon 추가
    :param pokemon:
    :return:
    """
    pokemons.append(None)
    pokemons[len(pokemons)-1] = pokemon

pokemons = []

if __name__ == "__main__":
    while True:
        menu = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))
        if (menu == 1):
            data = input("추가할 데이터--> ")
            add_data(data)
            print(pokemons)
        elif (menu == 2):
            pos = int(input("삽입할 위치--> "))
            data = input("추가할 데이터--> ")
            insert_data(pos, data)
            print(pokemons)
        elif (menu == 3):
            pos = int(input("삭제할 위치--> "))
            delete_data(pos)
            print(pokemons)
        elif (menu == 4):
            print(pokemons)
            # exit()
            break
        else:
            print("1~4 중 하나를 입력하세요.")
            continue
