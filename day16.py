import random
import math


class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_stores(start):
    current = start
    if current == None:
        return

    while True:
        if current.link == head:
            break
        current = current.link
        x, y = current.data[1:]
        print(current.data[0], '편의점, 거리:', math.sqrt(x * x + y * y))
    print()


def make_store_list(store):
    global c_linked_list, head, current, pre

    node = Node()
    node.data = store
    c_linked_list.append(node)

    if head == None:
        head = node
        node.link = head
        return

    nodeX, nodeY = node.data[1:]
    nodeDist = math.sqrt(nodeX ** 2 + nodeY ** 2)
    headX, headY = head.data[1:]
    headDist = math.sqrt(nodeX ** 2 + nodeY ** 2)

    if headDist > nodeDist:
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while True:
        if current.link == head:
            break
        pre = current
        current = current.link
        currX, currY = current.data[1:]
        currDist = math.sqrt(currX ** 2 + currY ** 2)
        if currDist > nodeDist:
            pre.link = node
            node.link = current
            return

    current.link = node
    node.link = head


c_linked_list = []
head, current, pre = None, None, None

if __name__ == "__main__":

    store_array = []
    store_name = 'A'
    for _ in range(10):
        store = (store_name, random.randint(1, 100), random.randint(1, 100))
        store_array.append(store)
        store_name = chr(ord(store_name) + 1)

    for store in store_array:
        make_store_list(store)

    print_stores(head)
