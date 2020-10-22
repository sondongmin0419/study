N, M = map(int, input().split())

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def play(y, x):
    for i in range(4):
        if x + dr[i] < 0 or x + dr[i] >= M or y + dc[i] < 0 or y + dc[i] >= N:
            li_w[y][x] = 0


    for i in range(4):
        if x + dr[i] < 0 or x + dr[i] >= M or y + dc[i] < 0 or y + dc[i] >= N:
            continue
        if li[y][x] + li_w[y][x] < li[y + dc[i]][x + dr[i]] + li_w[y + dc[i]][x + dr[i]]:
            li_w[y + dc[i]][x + dr[i]] -= li[y + dc[i]][x + dr[i]] + li_w[y + dc[i]][x + dr[i]] - (li[y][x] + li_w[y][x])
            if li_w[y + dc[i]][x + dr[i]] < 0:
                li_w[y + dc[i]][x + dr[i]] = 0
            stack.append([y + dc[i],  x + dr[i]])


li = [list(map(int, list(input()))) for _ in range(N)]
li_w = [[0] * M for _ in range(N)]
max_n = 0
for i in range(N):
    for j in range(M):
        if max_n < li[i][j]:
            max_n = li[i][j]

for i in range(N):
    for j in range(M):
        li_w[i][j] = max_n - li[i][j]
stack = []

for i in range(N):
    for j in range(M):
        play(i, j)
        while stack:
            yx = stack.pop(0)
            play(yx[0], yx[1])

result = 0
for i in range(N):
    for j in range(M):
        result += li_w[i][j]
print(result)