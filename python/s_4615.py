import sys
import copy
sys.stdin = open("sample__4615.txt", "r")

T = int(input())


def row(r, c):
    c1 = c
    if li_row[r][c1+1] != '':
        while 0<r<N and 0<c1<N:
            if li_row[r][c1+1] == li_row[r][c1]:
                return
            else:
                li_row[r][c1+1] = li_row[r][c1]
                li[r][c1+1] = li[r][c1]
            c1 += 1
    c2 = c
    if li_row[r][c-1] != '':
        while 0<r<N and 0<c<N:
            if li_row[r][c2-1] == li_row[r][c2]:
                return
            else:
                li_row[r][c2-1] = li_row[r][c2]
                li[r][c2-1] = li[r][c2]
            c2 -= 1


def col(r, c):
    r1 = r
    r2 = r
    if li_col[r1+1][c] != '':
        while 0<r1<N and 0<c<N:
            if li_col[r1+1][c] == li_col[r1][c]:
                return
            else:
                li_col[r1+1][c] = li_col[r1][c]
                li[r1+1][c] = li[r1][c]

            r1 += 1
    if li_col[r2 - 1][c] != '':
        while 0<r2<N and 0<c<N:
            if li_col[r2-1][c] == li_col[r2][c]:
                return
            else:
                li_col[r2-1][c] = li_col[r2][c]
                li[r2-1][c] = li[r2][c]

            r2 -= 1


def x(r, c):
    r1=r; c1=c
    r2=r; c2=c
    r3=r; c3=c
    r4=r; c4=c
    if li_x[r1+1][c1+1] != '':
        while 0<r1<N and 0<c1<N:
            if li_x[r1+1][c1+1] == li_x[r1][c1]:
                return
            else:
                li_x[r1+1][c1+1] = li_x[r1][c1]
                li[r1+1][c1+1] = li[r1][c1]

            c1 += 1
            r1 += 1
    if li_x[r2 + 1][c2 - 1] != '':
        while 0<r2<N and 0<c2<N:
            if li_x[r2+1][c2-1] == li_x[r2][c2]:
                return
            else:
                li_x[r2+1][c2-1] = li_x[r2][c2]
                li[r2+1][c2-1] = li[r2][c2]

            c2 -= 1
            r2 += 1
    if li_x[r3 - 1][c3 - 1] != '':
        while 0<r3<N and 0<c3<N:
            if li_x[r3-1][c3-1] == li_x[r3][c3]:
                return
            else:
                li_x[r3-1][c3-1] = li_x[r3][c3]
                li[r3-1][c3-1] = li[r3][c3]

            c3 -= 1
            r3 -= 1
    if li_x[r4 - 1][c4 + 1] != '':
        while 0<r4<N and 0<c4<N:
            if li_x[r4-1][c4+1] == li_x[r4][c4]:
                return
            else:
                li_x[r4-1][c4+1] = li_x[r4][c4]
                li[r4 - 1][c4 + 1] = li[r4][c4]
            c4 += 1
            r4 -= 1


for TC in range(1, T+1):

    N, M = map(int, input().split())
    li = [[''] * (N+2) for _ in range(N+2)]
    li[N // 2][N // 2] = 'W'
    li[N // 2 + 1][N // 2 + 1] = 'W'
    li[N // 2 + 1][N // 2] = 'B'
    li[N // 2][N // 2 + 1] = 'B'

    inputs = [list(map(int, input().split())) for _ in range(M)]
    print(inputs)
    for i in range(M):
        if inputs[i][2] == 1:
            li[inputs[i][0]][inputs[i][1]] = 'B'
        else:
            li[inputs[i][0]][inputs[i][1]] = 'W'
        li_row = copy.deepcopy(li)
        li_col = copy.deepcopy(li)
        li_x = copy.deepcopy(li)
        row(inputs[i][0], inputs[i][1])
        col(inputs[i][0], inputs[i][1])
        x(inputs[i][0], inputs[i][1])
        print(TC)
        for k in range(1,N+1):
            print(li[k])

    sum_B = 0
    sum_W = 0
    for p in range(1,N+1):
        for q in range(1,N+1):
            if li[p][q] == 'B':
                sum_B += 1
            elif li[p][q] == 'W':
                sum_W += 1
        print(sum_B, sum_W)
