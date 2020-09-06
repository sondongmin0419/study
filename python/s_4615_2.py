import sys
sys.stdin = open("sample__4615.txt", "r")


T = int(input())

for TC in range(1, T+1):

    N, M = map(int, input().split())
    li = [[''] * (N + 2) for _ in range(N + 2)]
    li[N // 2][N // 2] = 'W'
    li[N // 2 + 1][N // 2 + 1] = 'W'
    li[N // 2 + 1][N // 2] = 'B'
    li[N // 2][N // 2 + 1] = 'B'
    inputs = [list(map(int, input().split())) for _ in range(M)]

    for i in range(M):
        x = inputs[i][0]
        y = inputs[i][1]
        if inputs[i][2] == 1:
            li[y][x] = 'B'
        else:
            li[y][x] = 'W'
        # 가로
        stack = []
        r_x = [False, 0]
        l_x = [False, 0]
        for q in range(x+1,N+1):
            if li[y][q] == li[y][x]:
                r_x = [True, q]
                break
            if li[y][q] == '':
                break
        for q in range(x-1, 0, -1):
            if li[y][q] == li[y][x]:
                l_x = [True, q]
                break
            if li[y][q] == '':
                break
        # 세로
        u_y = [False, 0]
        d_y = [False, 0]
        for q in range(y+1,N+1):
            if li[q][x] == li[y][x]:
                u_y = [True, q]
                break
            if li[q][x] == '':
                break
        for q in range(y-1, 0, -1):
            if li[q][x] == li[y][x]:
                d_y = [True, q]
                break
            if li[q][x] == '':
                break
        #대각선
        ur_xy = [False, 0]
        ul_xy = [False, 0]
        dr_xy = [False, 0]
        dl_xy = [False, 0]

        for q in range(1, N):
            if li[y+q][x+q] == li[y][x]:
                dr_xy = [True, q]
                break
            if li[y+q][x+q] == '':
                break
                
        for q in range(1, N):
            if li[y+q][x-q] == li[y][x]:
                dl_xy = [True, q]
                break
            if li[y+q][x-q] == '':
                break
        for q in range(1, N):
            if li[y-q][x+q] == li[y][x]:
                ur_xy = [True, q]
                break
            if li[y-q][x+q] == '':
                break
        for q in range(1, N):
            if li[y-q][x-q] == li[y][x]:
                ul_xy = [True, q]
                break
            if li[y-q][x-q] == '':
                break

        if r_x[0]:
            for q in range(x+1,r_x[1]):
                li[y][q] = li[y][x]
        if l_x[0]:
            for q in range(l_x[1], x):
                li[y][q] = li[y][x]
        if u_y[0]:
            for q in range(y, u_y[1]):
                li[q][x] = li[y][x]
        if d_y[0]:
            for q in range(d_y[1], y):
                li[q][x] = li[y][x]
        if ur_xy[0]:
            for q in range(1, ur_xy[1]):
                li[y - q][x + q] = li[y][x]
        if ul_xy[0]:
            for q in range(1, ul_xy[1]):
                li[y - q][x - q] = li[y][x]
        if dr_xy[0]:
            for q in range(1, dr_xy[1]):
                li[y + q][x + q] = li[y][x]
        if dl_xy[0]:
            for q in range(1, dl_xy[1]):
                li[y + q][x - q] = li[y][x]
        # print(i)
        # for r in range(N+2):
        #     print(li[r])
    sum_B = 0
    sum_W = 0
    for p in range(1, N + 1):
        for q in range(1, N + 1):
            if li[p][q] == 'B':
                sum_B += 1
            elif li[p][q] == 'W':
                sum_W += 1
    print('#%d %d %d' % (TC, sum_B, sum_W))