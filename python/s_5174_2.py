T = int(input())


def play(n):
    global cnt
    q = []
    q.append(n)
    while q:
        n = q.pop(0)
        for i in range(len(li_v[n])):
            cnt += 1
            k = li_v[n].pop()
            q.append(k)
    return


for TC in range(1, T+1):
    E, N = map(int, input().split())
    li_v = [[] for _ in range(E+2)]
    li_input = list(map(int, input().split()))
    for i in range(E):
        li_v[li_input[i*2]].append(li_input[i*2 + 1])
    cnt = 1
    play(N)
    print('#%d %d' % (TC, cnt))