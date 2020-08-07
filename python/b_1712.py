a, b, c = map(int, input().split())

n = 0

if b >= c:
    print(-1)
else:
    while a+(b*n) >= c*n:
        n += 1
    print(n)
