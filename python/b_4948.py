import sys

li = []

for M in sys.stdin:

    M = int(M)

    N = 2 * M
    li_1 = [1] * (N+1)
    li_1[0] = 0
    li_1[1] = 0

    for i in range(2, N+1):
        k = 2
        if li_1[i] == 1:
            while i * k <= N:
                li_1[i*k] = 0
                k += 1
                if i * k > N:
                    break
    cnt = 0
    for i in range(M+1, M*2+1):
        if li_1[i] == 1:
            cnt += 1
    print(cnt)