import sys
input = sys.stdin.readline

N, M = map(int, input().split())

stu = [[] for _ in range(N)]

stu_n = [0] * N

for _ in range(M):
    a, b = map(int, input().split())

    stu[b].append(a)
    stu_n[b] += 1




