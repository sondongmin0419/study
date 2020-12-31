import sys

N = int(input())

li = [0]*10001

for _ in range(N):
    li[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    for k in range(li[i]):
        print(i)