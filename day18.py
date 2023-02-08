
class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


g1 = None
stack = []
stack_visited_ary = []

g1 = Graph(9)
g1.graph[0][1] = 1
g1.graph[0][2] = 1
g1.graph[0][4] = 1

g1.graph[1][0] = 1
g1.graph[1][2] = 1
g1.graph[1][3] = 1

g1.graph[2][0] = 1
g1.graph[2][1] = 1
g1.graph[2][3] = 1
g1.graph[2][4] = 1

g1.graph[3][1] = 1
g1.graph[3][2] = 1

g1.graph[4][0] = 1
g1.graph[4][2] = 1
g1.graph[4][7] = 1
g1.graph[4][6] = 1

g1.graph[5][2] = 1

g1.graph[6][4] = 1
g1.graph[6][8] = 1

g1.graph[7][4] = 1
g1.graph[7][8] = 1

g1.graph[8][7] = 1
g1.graph[8][6] = 1

for row in range(9):
    for col in range(9):
        print(g1.graph[row][col], end=' ')
    print()

current = 0
stack.append(current)
stack_visited_ary.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(9):
        if g1.graph[current][vertex] == 1:
            if vertex in stack_visited_ary:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        stack_visited_ary.append(current)
    else:
        current = stack.pop()

print('방문 순서 =', end='')
for i in stack_visited_ary:
    print(chr(ord('A') + i), end='   ')


# 너비우선탐색 큐 사용 fifo

from collections import deque

g2 = None
queue = deque([])
que_visited_ary = []

g2 = Graph(5)
g2.graph[0][2] = 1; g2.graph[0][3] = 1
g2.graph[1][2] = 1
g2.graph[2][0] = 1; g2.graph[2][1] = 1; g2.graph[2][3] = 1
g2.graph[3][0] = 1; g2.graph[3][2] = 1
g2.graph[4][0] = 1

print()
for row in range(5):
    for col in range(5):
        print(g2.graph[row][col], end=' ')
    print()

current = 0
queue.append(current)
que_visited_ary.append(current)

while len(queue) != 0:
    next = None
    for vertex in range(4):
        if g2.graph[current][vertex] == 1:
            if vertex in que_visited_ary:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        queue.append(current)
        que_visited_ary.append(current)
    else:
        # current = queue.pop(0)  # overhead
        current = queue.popleft()

print('방문 순서 =', end='')
for i in que_visited_ary:
    print(chr(ord('A') + i), end='   ')
