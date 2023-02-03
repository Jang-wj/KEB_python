pokemons = ["피카츄", "라이츄", '파이리', '꼬부기', '이상해']


def insert_data(idx, pokemon):
    if idx < 0 or idx > len(pokemons):
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return

    pokemons.append(None)  # 빈칸 추가

    for i in range(len(pokemons)-1, idx, -1):
        pokemons[i] = pokemons[i - 1]
        pokemons[i - 1] = None

    pokemons[idx] = pokemon  # 지정한 위치에 친구 추가


insert_data(2, '거북왕')
print(pokemons)
insert_data(6, '버터풀')
print(pokemons)
