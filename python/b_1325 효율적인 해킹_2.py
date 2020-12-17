import sys
from collections import deque

def dfs(n):
    global cnt
    cnt += 1
    arr = arr_N[n]
    if arr:
        for n_n in arr:
            if arr_result[n_n] != 0:
                cnt += arr_result[n_n]
            else:
                stack.append(n_n)
    else:
        arr_result[n] = 1
    return


input = sys.stdin.readline

N, M = map(int, input().split())
arr_N = [[] for _ in range(N + 1)]
arr_result = [0 for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    arr_N[B].append(A)

check = True

for i in range(1, N + 1):
    if visited[i] == 0:
        cnt = 1
        stack = deque()
        for j in arr_N[i]:
            if arr_result[j] != 0:
                cnt += arr_result[j]
            else:
                stack.append(j)
        while stack:
            num = stack.popleft()
            dfs(num)
        arr_result[i] = cnt

print(arr_result)
