T = int(input())

for TC in range(1, T+1):
    n = int(input())

    li = list(map(int, input(). split()))
    for i in range(n-1):
        for j in range(i, n):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]
    result1 = []
    result2 = []
    for i in range(n):
        if i >= n/2:
            result2.append(li[i])
        else:
            result1.append(li[i])
    result = []
    r1 = 0
    r2 = n//2-1
    for i in range(10):
        if i % 2 == 1:
            result += [result1[r1]]
            r1 += 1
        else:
            result += [result2[r2]]
            r2 -= 1
    print(f'#{TC} ', end='')
    for i in range(10):
        print(result[i], end=' ')
    print()
