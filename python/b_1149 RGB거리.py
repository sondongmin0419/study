import sys

input = sys.stdin.readline





N = int(input())

li = [list(map(int, input().split())) for _ in range(N)]
li_cost = [[0]*N for _ in range(3)]
li_cost[0][0] = li[0][0]
li_cost[1][0] = li[0][1]
li_cost[2][0] = li[0][2]

for i in range(1,N):
    for c in range(3):
        s = []
        for b_c in range(3):
            if c != b_c:
                s.append(li_cost[b_c][i-1] + li[i][c])
        li_cost[c][i] = min(s)

print(min(li_cost[0][N-1], li_cost[1][N-1], li_cost[2][N-1]))