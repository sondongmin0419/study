import sys
sys.setrecursionlimit(100000)

def dfs(n):
    cnt = 1
    for k in arr_N[n]:
        if k == i:
            arr_result[k] = -10
            arr_result[n] = 1
            return
        if arr_result[k] == 0:
            arr_result[k] = -1
            dfs(k)
        cnt += arr_result[k]
    if arr_result[n] == -10:
        stack = arr_N[n]
        while stack:
            for _ in range(len(stack)):
                t = stack.pop(0)
                arr_result[t] = cnt
                for n_t in arr_N[t]:
                    if arr_result[n_t] != cnt:
                        stack.append(n_t)
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
