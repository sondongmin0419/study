import sys

N = int(input())


def b_14889(n):
    global result
    if n >= N:
        return
    if sum(start_team) == N // 2:
        start_team_total = 0
        link_team_total = 0
        s = []
        l = []
        for i in range(N):
            if start_team[i] == 0:
                l.append(i)
            else:
                s.append(i)
        for i in range(N // 2):
            for j in range(N // 2):
                start_team_total += arr[s[i]][s[j]]
                link_team_total += arr[l[i]][l[j]]
        p = abs(start_team_total - link_team_total)
        if p < result:
            result = p
        return
    if sum(start_team) < N // 2:
        start_team[n] = 1
        b_14889(n + 1)
        start_team[n] = 0
        b_14889(n + 1)
    return


arr = [list(map(int, input().split())) for _ in range(N)]

start_team = [0] * N
link_team = []

result = sys.maxsize
b_14889(0)
print(result)
