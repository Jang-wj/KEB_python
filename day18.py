class Graph:
    def __init__(self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print(' ', end=' ')
    for v in range(g.SIZE):
        print(cities[v], end=' ')
    print()
    for row in range(g.SIZE):
        print(cities[row], end=' ')
        for col in range(g.SIZE):
            print("%4d" % g.graph[row][col], end=' ')
        print()
    print()


def find_vertex(g, find_vt):
    stack = []
    visited_ary = []

    current = 0
    stack.append(current)
    visited_ary.append(current)

    while len(stack) != 0:
        next = None
        for vertex in range(g_size):
            if g.graph[current][vertex] != 0:
                if vertex in visited_ary:
                    pass
                else:
                    next = vertex
                    break

        if next is not None:
            current = next
            stack.append(current)
            visited_ary.append(current)
        else:
            current = stack.pop()

    if find_vt in visited_ary:
        return True
    else:
        return False




cities = ['서울', '뉴욕', '런던', '북경', '방콕', '파리']
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5


g_size = len(cities)
g = Graph(g_size)
g.graph[서울][뉴욕] = 80
g.graph[서울][북경] = 10
g.graph[뉴욕][서울] = 80
g.graph[뉴욕][북경] = 40
g.graph[뉴욕][방콕] = 70
g.graph[런던][방콕] = 30
g.graph[런던][파리] = 60
g.graph[북경][서울] = 10
g.graph[북경][뉴욕] = 40
g.graph[북경][방콕] = 50
g.graph[방콕][뉴욕] = 70
g.graph[방콕][북경] = 50
g.graph[방콕][런던] = 30
g.graph[방콕][파리] = 20
g.graph[파리][방콕] = 20
g.graph[파리][런던] = 60

print('## 전체 연결도 ##')
print_graph(g)

edge_ary = []
for i in range(g_size):
    for k in range(g_size):
        if g.graph[i][k] != 0:
            edge_ary.append([g.graph[i][k], i, k])

from operator import itemgetter

edge_ary = sorted(edge_ary, key=itemgetter(0), reverse=False)

new_ary = []
for i in range(0, len(edge_ary), 2):
    new_ary.append(edge_ary[i])

index = 0
while len(new_ary) > g_size - 1:
    start = new_ary[index][1]
    end = new_ary[index][2]
    saveCost = new_ary[index][0]

    g.graph[start][end] = 0
    g.graph[end][start] = 0

    start_yn = find_vertex(g, start)
    end_yn = find_vertex(g, end)

    if start_yn and end_yn:
        del (new_ary[index])
    else:
        g.graph[start][end] = saveCost
        g.graph[end][start] = saveCost
        index += 1

print('## 가장 효율적인 연결도 ##')
print_graph(g)
