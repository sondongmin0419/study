import sys
sys.setrecursionlimit(100000)

def dfs(n):
    cnt = 1
    for k in arr_N[n]:
        # if k == i:
        #     arr_result[n] = 0
        #     return
        if arr_result[k] == 0:
            arr_result[k] = -1
            dfs(k)
        cnt += arr_result[k]
    arr_result[n] = cnt
    return


input = sys.stdin.readline

N, M = map(int, input().split())
arr_N = [[] for _ in range(N + 1)]
arr_result = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    arr_N[B].append(A)

max_n = 0
for i in range(1, N + 1):
    if arr_result[i] == 0:
        dfs(i)
        if arr_result[i] > max_n:
            max_n = arr_result[i]

stack = []
for i in range(1, N+1):
    if arr_result[i] == max_n:
        stack.append(i)

print(*stack)
