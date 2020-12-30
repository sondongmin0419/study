N = int(input())

result = 0
for i in range(1, N):
    n = i
    s = n
    while n > 0:
        s += n % 10
        n = n // 10
    if s == N:
        result = i
        break

print(result)
