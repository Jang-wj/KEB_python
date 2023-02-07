import random


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


def preorder(node):
    if not node:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


memory = []
root = None
data_array = ['바나나맛우유', '레쓰비캔커피', '츄파춥스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sell_array = [random.choice(data_array) for i in range(20)]

print('오늘 판매된 물건(중복O) -->', sell_array)

node = TreeNode()
node.data = sell_array[0]
root = node
memory.append(node)

for name in sell_array[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name == current.data:
            break
        if name < current.data:
            if not current.left:
                current.left = node
                memory.append(node)
                break
            current = current.left
        else:
            if not current.right:
                current.right = node
                memory.append(node)
                break
            current = current.right

print("이진 탐색 트리 구성 완료!")
print('오늘 판매된 종류(중복X) : ', end=' ')
preorder(root)
