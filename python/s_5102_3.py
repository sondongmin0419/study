T = int(input())


def play(s):
    global result
    global cnt
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        cnt += 1
        for i in range(len(q)):
            k = q.pop(0)
            for j in range(len(li_v[k])):
                k_k = li_v[k].pop(0)
                if k_k == G:
                    result = 1
                    return
                elif visited[k_k] == 0:
                    q.append(k_k)
                    visited[k_k] = 1
    return


for TC in range(1, T+1):
    V, E = map(int, input().split())
    li_v = [[] for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int, input().split())
        li_v[a].append(b)
        li_v[b].append(a)
    S, G = map(int, input().split())
    visited = [0] * (V+1)
    result = 0
    cnt = 0
    if S != G:
        play(S)
    if result == 0:
        print('#%d %d' % (TC, 0))
    else:
        print('#%d %d' % (TC, cnt))
