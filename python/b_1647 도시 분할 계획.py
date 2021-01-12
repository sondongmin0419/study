import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int, input().split())
    arr[a].append([b,c])
visited = [False] * N

for i in range(N+1):
    arr[i].sort(key=lambda x : x[1])

now = []
for i in range(N+1):
    if arr[i]:
        now = arr[i][0]
        break
result = 0
while True:
    if not visited[now[0]]:
        visited[now[0]] = True
        result += now[1]
        now =



print(arr)