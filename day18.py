class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g):
    print('	', end='')
    for v in range(g.size):
        print("%9s" % stores[v][0], end=' ')
    print()
    for row in range(g.size):
        print("%9s" % stores[row][0], end=' ')
        for col in range(g.size):
            print("%8d" % g.graph[row][col], end=' ')
        print()
    print()


g = None
stores = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
GS25, CU, Seven11, MiniStop, Emart24 = 0, 1, 2, 3, 4

g_size = len(stores)
g = Graph(g_size)
g.graph[GS25][CU] = 1; g.graph[GS25][Seven11] = 1
g.graph[CU][GS25] = 1; g.graph[CU][Seven11] = 1; g.graph[CU][MiniStop] = 1
g.graph[Seven11][GS25] = 1; g.graph[Seven11][CU] = 1; g.graph[Seven11][MiniStop] = 1
g.graph[MiniStop][Seven11] = 1; g.graph[MiniStop][CU] = 1; g.graph[MiniStop][Emart24] = 1
g.graph[Emart24][MiniStop] = 1

print_graph(g)

stack = []
visited = []

current = 0
max_store = current
max_count = stores[current][1]
stack.append(current)
visited.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(g_size):
        if g.graph[current][vertex] == 1:
            if vertex in visited:
                pass
            else:
                next = vertex
                break

    if next != None:
        current = next
        stack.append(current)
        visited.append(current)
        if stores[current][1] > max_count:
            max_count = stores[current][1]
            max_store = current
    else:
        current = stack.pop()

print(f'max_store(count) = {stores[max_store][0]} ({stores[max_store][1]})')
