M, N = map(int, input().split())

li = [1] * (N+1)
li[0] = 0
li[1] = 0
for i in range(2, N+1):
    k = 2
    if li[i] == 1:
        while i * k <= N:
            li[i*k] = 0
            k += 1
            if i * k > N:
                break

for i in range(M, N+1):
    if li[i] == 1:
        print(i)