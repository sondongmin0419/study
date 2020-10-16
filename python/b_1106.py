def min_money(li_m, c_m, c_min):
    r = [0]*(c_m+5)
    for j in range(1, c_m+1):
        q = 999999
        for i in range(1, j+1):
            if li_m[i] != 0:
                q = min(q, li_m[i] + r[j-i])
        r[j] = q
    result = min(r[c_min:c_m+1])
    return result


C, N = map(int, input().split())
li = [0]*(C+101)
max_index = 0


for TC in range(N):
    mini = list(map(int, input().split()))   # [비용 , 고객수]
    k = 1
    while True:
        if li[mini[1]*k] > mini[0]*k or li[mini[1]*k] == 0:
            li[mini[1]*k] = mini[0]*k
        k += 1
        if mini[1]*k >= C + 101:
            k -= 1
            if max_index < mini[1]*k:
                max_index = mini[1]*k
            break

print(min_money(li, max_index, C))