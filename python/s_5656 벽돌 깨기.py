def dfs(test_li):
    global cnt
    global min_n
    if cnt == N:
        total = 0
        for i in range(W):
            for j in range(H):
                if test_li[j][i]>0:
                    total += 1
        if min_n > total:
            min_n = total
        return

    for w in range(W):
        for h in range(H):
            li_ = test_li[:]
            if li_[h][w] > 0:
                cnt += 1
                k = li_[h][w]
                li_[h][w] = 0
                if k > 1:
                    boom(w, h, k, li_)
                    for ww in range(W):
                        for hh in range(H - 1, 0, -1):
                            if li_[hh][ww] == 0:
                                for kk in range(hh + 1, H):
                                    if li_[kk][ww] > 0:
                                        li_[hh][ww] = li_[kk][ww]
                                        li_[kk][ww] = 0
                dfs(li_)
                cnt -= 1
    return


def boom(w, h, k, li_):
    for i in range(1, k + 1):
        if 0 < w + i < W:
            kk = li_[h][w + i]
            li_[h][w + i] = 0
            boom(w, h, kk, li_)
        if 0 < w - i < W:
            kk = li_[h][w - i]
            li_[h][w - i] = 0
            boom(w, h, kk, li_)
        if 0 < h + i < H:
            kk = li_[h + i][w]
            li_[h + i][w] = 0
            boom(w, h, kk, li_)
        if 0 < h - i < H:
            kk = li_[h - i][w]
            li_[h - i][w] = 0
            boom(w, h, kk, li_)


T = int(input())

for TC in range(1, T + 1):
    N, W, H = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(H)]
    cnt = 0
    min_n = W*H
    for i in range(N):
        dfs(li)
    print(min_n)
