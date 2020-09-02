import sys
sys.stdin = open("input_1.txt", "r")


def play(i_c):
    global total
    global min_n

    for i in range(N):
        if li_check[i] == 0:
            total += li[i_c][i]
            li_check[i] = 1
            if total > min_n:
                total -= li[i_c][i]
                li_check[i] = 0
                continue
            if i_c == N - 1:
                if total < min_n:
                    min_n = total
                total -= li[i_c][i]
                li_check[i] = 0
                return 0
            play(i_c+1)
            total -= li[i_c][i]
            li_check[i] = 0


T = int(input())

for TC in range(1, T+1):

    N = int(input())
    min_n = 10*10
    total = 0
    li = [list(map(int, input().split())) for _ in range(N)]
    li_check = [0] * N

    play(0)

    print('#%d %d' % (TC, min_n))


