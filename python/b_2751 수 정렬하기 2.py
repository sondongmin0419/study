import sys

N = int(input())

li = []

for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))

li.sort()

for i in range(N):
    print(li[i])