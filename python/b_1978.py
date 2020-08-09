T = int(input())

li = list(map(int, input().split()))
t_cnt = 0

for TC in range(T):
    cnt = 0
    for i in range(1, li[TC]+1):
        if li[TC] == 1:
            break
        elif li[TC] % i == 0:
            cnt += 1
    if cnt == 2:
        t_cnt += 1
print(t_cnt)