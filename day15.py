def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons)-1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가

def delete_data(idx):
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


if __name__ == "__main__":
    pokemons = ["피카츄", "라이츄", "꼬부기", "파이리", "이상해"]
    print(pokemons)
    insert_data(3, '어니부기')
    print(pokemons)
    insert_data(6, '거북왕')
    print(pokemons)
    delete_data(1)
    print(pokemons)
