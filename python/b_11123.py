T = int(input())

H, W = map(int, input().split())

li = [[0] for _ in range(H)]
for h in range(H):
    li[h] = list(input())

cnt = 0

for h in range(H):
    for w in range(W):
        result = 0
        if h == 0:
            if w == 0:
                if li[h][w+1] == '#' or li[h+1][w]:
                    result += 1
            elif w == W-1
                if li[h][w - 1] == '#' or li[h + 1][w]:
                    result += 1
            else:
        elif h == H-1:
            if w == 0:
                pass
            elif w == W-1
                pass
            else:
        else:
            if w == 0:
                pass
            elif w == W-1
                pass
            else: