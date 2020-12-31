import sys

input = sys.stdin.readline

N = int(input())

li = [input().rstrip() for _ in range(N)]
li = list(set(li))
li.sort(key=lambda x: (len(x), x))
for i in range(len(li)):
    print(li[i])
