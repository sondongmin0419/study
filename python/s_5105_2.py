T = int(input())

dr = [0, 1, 0, -1]  # 상 우 하 좌
dc = [-1, 0, 1, 0]

def play(y, x):
    global result
    for i in range(4):
        ny = y+dc[i]
        nx = x+dr[i]
        if 0 <= ny < N and 0 <= nx < N and li_v[ny][nx] == 0:
            if li[ny][nx] == '3':
                result = 1
                return
            elif li[ny][nx] == '0':
                q.append((ny,nx))
                li_v[ny][nx] = 1




for TC in range(1, T+1):
    N = int(input())
    result = 0
    li = []
    y,x = (-1,-1)
    cnt = 0
    for i in range(N):
        li.append(list(input()))
        if y == -1:
            for j in range(N):
                if li[i][j] == '2':
                    (y,x) = (i, j)
    li_v = [[0] * N for _ in range(N)]
    q = []
    q.append((y,x))
    y, x = q.pop(0)
    play(y, x)
    while q:
        cnt += 1
        len_q = len(q)
        for i in range(len_q):
            y, x = q.pop(0)
            play(y, x)
            if result == 1:
                q = []
                break
    print('#%d ' % TC, end='')
    if result == 1:
        print(cnt)
    else:
        print(0)