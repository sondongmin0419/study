import sys

input = sys.stdin.readline
N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]

li.sort(key=lambda x: (x[0], x[1]))
for i in range(N):
    print(li[i][0], li[i][1])