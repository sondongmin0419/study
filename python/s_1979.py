import sys
sys.stdin = open("input_1979.txt", "r")


T = int(input())
for TC in range(1, T+1):
    N, K = map(int, input().split())

    li = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    for i in range(N):
        r_r = 0
        r_c = 0
        cnt_r = 0
        cnt_c = 0
        for j in range(N):
            if li[i][j] == 1:
                cnt_r += 1
            else:
                if cnt_r == K:
                    r_r += 1
                cnt_r = 0
            if li[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    r_c += 1
                cnt_c = 0
        if cnt_r == K:
            r_r += 1
        if cnt_c == K:
            r_c += 1
        total += r_c + r_r
    print('#%d %d' % (TC, total))