import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
arr_N = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    arr_N[B].append(A)

check = True
result = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    cnt = 1
    stack = deque()
    stack.append(i)
    while stack:
        n = stack.popleft()
        visited[n] = 1
        if arr_N[n]:
            for j in arr_N[n]:
                if visited[j] == 0:
                    cnt += 1
                    stack.append(j)
                    visited[j] = 1
    result[i] = cnt
max_ = max(result)
for i in range(1,N+1):
    if result[i] == max_:
        print(i , end=' ')
