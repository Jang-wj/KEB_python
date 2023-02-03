def printPoly(px):
    """
    다항식을 포맷에 맞게 출력
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 문자열
    """
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1
    poly_str = "P(x) = "

    for i in range(len(px)):
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


def calcPoly(x_val, px):
    """
    다항식을 계산
    :param x_val: x 값 integer
    :param px: 계수를 원소로 가지고 있는 list
    :return: 다항식 계산 결과 값 integer
    """
    ret_value = 0
    term = len(px) - 1  # 최고차항 숫자 = 배열길이-1

    for i in range(len(px)):
        coef = px[i]  # 계수
        ret_value += coef * xValue ** term
        term -= 1

    return ret_value


px = [3, -4, 0, 6]  # = 3x^3 -4x^2 +0x^1 +6x^0


if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값-->"))

    pxValue = calcPoly(xValue, px)
    print(pxValue)


