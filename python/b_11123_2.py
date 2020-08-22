def group(h, w):
    total = 0
    if li[h][w] == ".":
        return 0
    else:
        li[h][w] = "@"
        if w + 1 != W:
            if li[h][w + 1] == "@":
                total += 1
            if li[h][w + 1] == "#":
                li[h][w] = "@"
        if h + 1 != H:
            if li[h + 1][w] == "@":
                total += 1
            if li[h+1][w] == "#":
                li[h+1][w] = "@"
        if w != 0:
            if li[h][w - 1] == "@":
                total += 1
            if li[h][w - 1] == "#":
                li[h][w - 1] = "@"
        if h != 0:
            if li[h-1][w] == "@":
                total += 1
            if li[h-1][w] == "#":
                li[h-1][w] = "@"

    if total == 0:
        return 1
    else:
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
