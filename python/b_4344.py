n = int(input())

li = [0] * n

for i in range(n):
    li[i] = list(map(int,input().split()))
    
for i in range(n):
    cnt = 0
    total = 0
    for k in range(1,len(li[i])):
        total += li[i][k]
    li_avg = total / li[i][0]
    for j in range(1,len(li[i])):
        if li[i][j] > li_avg:
            cnt += 1
    result = (cnt/li[i][0]) * 100
    # print(f'{round(result,3)}%')
    print('%.3f' % result,end='')
    print('%')
