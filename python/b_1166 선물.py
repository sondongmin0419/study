N, L, W, H = map(int, input().split())

li = [L, W, H]

li.sort()
r = li[0]
l = 0
m = (r + l) // 2
for _ in range(60):
    m = (l + r) / 2
    total = (li[0] // m) * (li[1] // m) * (li[2] // m)
    if total < N:
        r = m
    else:
        l = m
print(r, m)
