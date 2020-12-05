import sys

N, M = map(int, sys.stdin.readline().strip().split())

li = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

li.sort(key=lambda x: (x[1], -x[0]))

meet = 0
money = 0
check = 0
for i in range(len(li)):
    meet += li[i][0]
    if meet < M:
        if i >= 1 and (li[i][1] == li[i - 1][1]):
            money += li[i][1]
        else:
            money = li[i][1]
    else:
        check = 1
        if i >= 1 and (li[i][1] == li[i - 1][1]):
            money += li[i][1]
            for j in range(i + 1, len(li)):
                if li[j][1] != li[i][1]:
                    if money > li[j][1]:
                        money = li[j][1]
                        break
        else:
            money = li[i][1]

        break

if check == 1:
    print(money)
else:
    print(-1)
