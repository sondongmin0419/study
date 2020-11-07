def BFS(v_s):
    for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
        nr = v_s[0] + dr
        nc = v_s[1] + dc

        if 0 <= nr < N and 0 <= nc < N and li_v[nr][nc] > li_v[v_s[0]][v_s[1]] + li[nr][nc]:
            li_v[nr][nc] = li_v[v_s[0]][v_s[1]] + li[nr][nc]
            stack.append((nr, nc))


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    li = [list(map(int, list(input()))) for _ in range(N)]
    li_v = [[1000000] * N for _ in range(N)]
    li_v[0][0] = 0
    cnt = 0
    min_cnt = 0
    stack = [(0,0)]
    while stack:
        stack = list(set(stack))
        s = len(stack)
        for _ in range(s):
            n_v = stack.pop(0)
            BFS(n_v)
    print('#%d %d' %(TC,li_v[N-1][N-1]))