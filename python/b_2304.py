N = int(input())

li = [0]*1001
for i in range(N):
    L, H = map(int, input().split())
    li[L] = H
max_h = max(li)
area = 0
h_l = li[1]
i_l = 1
while li[i_l] < max_h:
    h_l = max(h_l, li[i_l])
    area += h_l
    i_l += 1
h_r = li[1000]
i_r = 1000
while i_r >= i_l:
    h_r = max(h_r, li[i_r])
    area += h_r
    i_r -= 1

print(area)