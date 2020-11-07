def kruskal():
    A = 0
    for v in range(V+1):
        make_set(dic, v)

    for i in range(E):
        if Find_set(dic, hq[i][1]) != Find_set(dic, hq[i][2]):
            A += hq[i][0]
            Union(dic, hq[i][1], hq[i][2])
    return A


def make_set(parent, x):
    if x not in hq:
        parent[x] = x


def Find_set(parent, x):
    if x == parent[x]:
        return x
    else:
        return Find_set(dic, parent[x])


def Union(parent, a, b):
    parent[Find_set(dic, b)] = a


T = int(input())

for TC in range(1, T + 1):
    V, E = map(int, input().split())
    dic = {}
    hq = []
    result = 0
    for i in range(E):
        n1, n2, w = map(int, input().split())
        hq.append([w, n1, n2])
    hq.sort()
    print('#%d %d' % (TC, kruskal()))
