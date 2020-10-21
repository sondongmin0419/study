N, M = map(int, input().split())

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]


def play(y, x):
    v_set = set()
    visited = []
    for i in range(4):
        if x + dr[i] < 0 or x + dr[i] >= M:
            return
        if y + dc[i] < 0 or y + dr[i] >= N:
            return
        
    for i in range(4):
        v_set.add(li[y+dc[i]][x+dr[i]])
    visited.append([y,x])



    pass


li = [list(map(int, input().split())) for _ in range(N)]


resutl = 0
for i in range(N):
    for j in range(M):
        play(i, j)