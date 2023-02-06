# 응용예제 4-2

import random

class Node():
    def __init__(self):
        self.data = None
        self.link = None


def print_nodes(start):
    current = start
    print(current.data, end=' ')
    while True:
        if current.link == None:
            break
        current = current.link
        print(current.data, end=' ')
    print()


def make_lotto_list(num):
    global linked_list, current, head, pre

    node = Node()
    node.data = num
    linked_list.append(node)
    if head == None:
        head = node
        return

    if head.data > num:
        node.link = head
        head = node
        return

    current = head
    while True:
        if current.link == None:
            break
        pre = current
        current = current.link
        if current.data > num:
            pre.link = node
            node.link = current
            return

    current.link = node

def find_lotto(num):
    global linked_list, head, current, pre

    if head == None:
        return False
    current = head
    if current.data == num:
        return True
    while True:
        if current.link == None:
            break
        current = current.link
        if current.data == num:
            return True
    return False



linked_list = []
head, current, pre = None, None, None

if __name__ == "__main__":
    cnt = 0
    while cnt <= 6:
        num = random.randint(1, 45)
        if find_lotto(num):
            continue
        make_lotto_list(num)
        cnt += 1

    print_nodes(head)

