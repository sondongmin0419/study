M, N = map(int, input().split())

for i in range(M, N+1):
    cnt = 0
    for j in range(1, int((i+1)**0.5)+1):
        if i % j == 0:
            cnt += 1
        if cnt > 1:
            break
    if cnt == 1:
        print(i)

