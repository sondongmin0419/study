import sys

T = int(input())

tc = [0] * T
for i in range(T):
    tc[i] = int(sys.stdin.readline())

max_tc = max(tc)
li = max_tc

tr_r = [0] * (1 + max_tc)

tr_r[:10] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(10, max_tc + 1):
    tr_r[i] = tr_r[i-1] + tr_r[i-5]

for i in tc:
    print(tr_r[i-1])