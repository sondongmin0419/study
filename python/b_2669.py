li = [[0] * 101 for _ in range(101)]
cnt = 0

for i in range(4):
    x, y, p, q = map(int, input().split())
    for c in range(y, q):
        for r in range(x, p):
            if li[c][r] == 0:
                cnt += 1
            li[c][r] = 1
print(cnt)