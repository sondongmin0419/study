import sys
input = sys.stdin.readline

N = int(input())

li = [list(map(str, input().rstrip().split())) for _ in range(N)]
li.sort(key = lambda x : int(x[0]))

for i in range(N):
    print(li[i][0], li[i][1])