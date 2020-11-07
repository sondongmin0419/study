def BFS(n):
    print(n+1)
    for i in range(N):
        if li_v[n][i] == 1 and v[i] == 0:
            li_v[n][i] = 0
            li_v[i][n] = 0
            stack.append(i)
            v[i] = 1
    if stack:
        BFS(stack.pop(0))


li = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = max(li)
li_v = [[0] * N for _ in range(N)]
v = [0] * N
stack = []
for _ in range(len(li)//2):
    i = li.pop(0)-1
    j = li.pop(0)-1
    li_v[i][j] = 1
    li_v[j][i] = 1
v[0] = 1
BFS(0)
