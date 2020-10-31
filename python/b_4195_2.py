import sys


def getParent(parents, x):
    if parents[x] == x:
        return x
    p = getParent(parents, parents[x])
    parents[x] = p
    return p


def unionParent(parents, x1, x2, cnt):
    a = getParent(parents, x1)
    b = getParent(parents, x2)
    if a!=b:
        parents[b] = a
        cnt[a] += cnt[b]


def findParent(x, parents):
    if parents[x] == x:
        return x
    return findParent(parents[x], parents)


T = int(sys.stdin.readline())

for TC in range(1, T+1):
    F = int(input())
    p_li = {}
    cnt = {}
    for _ in range(F):
        p1, p2 = sys.stdin.readline().split()
        if p1 not in p_li:
            p_li[p1] = p1
            cnt[p1] = 1
        if p2 not in p_li:
            p_li[p2] = p2
            cnt[p2] = 1
        unionParent(p_li, getParent(p_li, p1), getParent(p_li, p2), cnt)

        print(cnt[findParent(p1, p_li)])