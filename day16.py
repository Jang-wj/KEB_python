import random


## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None


def printNodes(start):
    current = start
    if current.link == None:
        return
    print(current.data, end=' ')
    while current.link != start:
        current = current.link
        print(current.data, end=' ')
    print()


def count_plus_minus():
    global head, current

    plus, minus, zero = 0, 0, 0

    current = head
    while True:
        if current.data > 0:
            plus += 1
        elif current.data < 0:
            minus += 1
        else:
            zero += 1
        if current.link == head:
            break
        current = current.link

    return plus, minus, zero


def makeMinusNumber():
    current = head
    while True:
        current.data *= -1
        if current.link == head:
            break
        current = current.link


## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__":

    dataArray = []
    for _ in range(7):
        dataArray.append(random.randint(-100, 100))

    node = Node()
    node.data = dataArray[0]
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    printNodes(head)
    count = count_plus_minus()
    print(f"양수 = {count[0]} 음수 = {count[1]} 0 = {count[2]}")
    makeMinusNumber()

    printNodes(head)
