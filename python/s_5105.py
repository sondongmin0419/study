import sys
sys.stdin = open("input_2.txt", "r")

def start_check():
    for i in range(N):
        for j in range(N):
            if li[i][j] == '2':
                return i, j


def play(i, j):
    global cnt
    global min_cnt
    li[i][j] = 1
    if cnt > min_cnt:
        cnt -= 1
        return i, j

    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]
    for k in range(4):
        i_n = i+dc[k]
        j_n = j+dr[k]
        if 0 <= i_n < N and 0 <= j_n < N:
            if li[i_n][j_n] == '0':
                cnt += 1
                stack.append((i, j))
                return i_n, j_n
            elif li[i_n][j_n] == '3':
                if min_cnt > cnt:
                    min_cnt = cnt
                return 101, 101
    cnt -= 1
    return 101, 101


T = int(input())

for TC in range(1, T+1):

    N = int(input())

    li = [list(input()) for _ in range(N)]
    st_i = 0
    st_j = 0
    st_i, st_j = start_check()
    cnt = 0
    min_cnt = 100*100
    stack = []
    result = []

    while True:
        y, x = play(st_i, st_j)
        st_i, st_j = y, x
        if len(stack) == 0:
            break
        if y == 101:
            st_i, st_j = stack.pop()
    if min_cnt == 100*100:
        print('#%d %d' % (TC, 0))
    else:
        print('#%d %d' % (TC, min_cnt))