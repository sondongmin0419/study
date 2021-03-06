import sys
sys.setrecursionlimit(10**6)


def group(h, w):
    if li[h][w] == ".":
        return 0
    elif li[h][w] == "#":
        li[h][w] = "@"
        if w + 1 != W:
            if li[h][w+1] == "#":
                group(h, w+1)
        if h + 1 != H:
            if li[h+1][w] == "#":
                group(h+1, w)
        if w != 0:
            if li[h][w-1] == "#":
                group(h, w-1)
        if h != 0:
            if li[h-1][w] == "#":
                group(h-1, w)
        return 1
    else:
        if w + 1 != W:
            if li[h][w+1] == "#":
                group(h, w+1)
        if h + 1 != H:
            if li[h+1][w] == "#":
                group(h+1, w)
        if w != 0:
            if li[h][w-1] == "#":
                group(h, w-1)
        if h != 0:
            if li[h-1][w] == "#":
                group(h-1, w)
        return 0


T = int(input())


for TC in range(T):
    global H, W

    H, W = map(int, input().split())

    global li
    li = [[0] for _ in range(H)]

    for k in range(H):
        li[k] = list(input())

    cnt = 0

    for high in range(H):
        for wide in range(W):
            cnt += group(high, wide)
    print(cnt)
