import sys
sys.stdin = open("input_5174.txt", "r")


def play(n):
    global cnt
    for i in range(len(li_c[n])):
        if li_c[n][i] != 0:
            cnt += 1
            play(li_c[n][i])



T = int(input())

for TC in range(1, T+1):
    E, N = map(int, input().split())

    li = list(map(int, input().split()))
    li_c = [[0]*2 for _ in range(E+2)]

    for i in range(E):
        if li_c[li[i*2]][0] == 0:
            li_c[li[i*2]][0] = li[i*2+1]
        else:
            li_c[li[i * 2]][1] = li[i*2+1]
    cnt = 1
    play(N)

    print('#%d %d' % (TC, cnt))