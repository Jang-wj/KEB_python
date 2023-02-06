# 응용예제 4-1

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


def make_linked_list(data):
    global linked_list, current, head, pre

    node = Node()
    node.data = data
    linked_list.append(node)
    if head == None:
        head = node
        return

    if head.data[1] > data[1]:
        node.link = head
        head = node
        return

    current = head
    while True:
        if current.link == None:
            break
        pre = current
        current = current.link
        if current.data[1] > data[1]:
            pre.link = node
            node.link = current
            return

    current.link = node


linked_list = []
head, current, pre = None, None, None

if __name__ == "__main__":
    while True:
        name = input("name :")
        if name == '' or name == None:
            break
        email = input("email :")
        make_linked_list([name, email])
        print_nodes(head)

