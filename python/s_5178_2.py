T = int(input())


def play(l):
    if l*2 <= N:
        return play(l*2) + play(l*2+1)
    else:
        leap = li_v[l]
        return leap


for TC in range(1, T+1):
    N, M, L = map(int, input().split())
    li_v = [0] * (N+2)
    for _ in range(M):
        a, b = map(int, input().split())
        li_v[a] = b

    result = play(L)
    print('#%d %d' % (TC, result))