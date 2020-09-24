w, h = map(int, input().split())

N = int(input())

rc_li = [[] for _ in range(2)]
rc_li[0].append(0)
rc_li[0].append(h)

rc_li[1].append(0)
rc_li[1].append(w)

for i in range(N):
    rc, n = map(int, input().split())
    rc_li[rc].append(n)
rc_li[0].sort()
rc_li[1].sort()
r_max = 0
h_max = 0
for i in range(1, len(rc_li[0])):
    r_max = max(r_max, rc_li[0][i]-rc_li[0][i-1])

for i in range(1, len(rc_li[1])):
    h_max = max(h_max, rc_li[1][i]-rc_li[1][i-1])
print(r_max * h_max)