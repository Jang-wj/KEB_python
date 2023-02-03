def printPoly(tx, px):
    """
    다항식을 포맷에 맞게 출력
    :param tx: 차수를 원소로 가지고 있는 list
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 문자열
    """
    poly_str = "P(x) = "

    for i in range(len(px)):
        term = tx[i]  # 차수
        coef = px[i]  # 계수

        if coef > 0 and i > 0:
            poly_str += "+"
        elif coef < 0:
            poly_str += ""
        elif coef == 0:
            term -= 1
            continue

        poly_str += f'{coef}x^{term} '
        term -= 1

    return poly_str


def calcPoly(tx, px):
    """
    다항식을 계산
    :param tx: 차수를 원소로 가지고 있는 list
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 계산 결과 값 integer
    """
    ret_value = 0

    for i in range(len(px)):
        term = tx[i]
        coef = px[i]  # 계수
        ret_value += coef * x_value ** term
        term -= 1

    return ret_value


tx = [300, 20, 0]
px = [7, -4, 5]


if __name__ == "__main__":
    pStr = printPoly(tx, px)
    print(pStr)

    x_value = int(input("X 값-->"))

    px_value = calcPoly(tx, px)
    print(px_value)


