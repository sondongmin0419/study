C, R = map(int, input().split())
K = int(input())


dr = [0, 1, 0, -1] # 상 우 하 좌
dc = [1, 0, -1, 0]
def play():
    x = y =1
    cnt = 1
    li[y][x] = cnt
    while cnt < K:
        for i in range(4):
            while True:
                ny = y + dc[i]
                nx = x + dr[i]
                if 1 <= nx <= C and 1 <= ny <= R and li[ny][nx] == 0:
                    cnt += 1
                    li[ny][nx] = cnt
                    if cnt == K:
                        return ny, nx
                else:
                    break
                x = nx
                y = ny
    return y, x

li = [[0] * (C+1) for _ in range(R+1)]

if K > C*R:
    print(0)
else:
    y, x = play()
    print(x, y)