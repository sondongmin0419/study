import sys
input = sys.stdin.readline

li_tc = []

while True:
    n = int(input())
    if n == 0:
        break
    li_tc.append(n)

max_tc = max(li_tc)
li = [0 for _ in range(max_tc + 1)]
li_ = []
for i in range(2, max_tc // 2):
    if li[i] == 0:
        for j in range(i * 2, max_tc + 1, i):
            li[j] = 1

for tc in li_tc:
    s_n = 0
    b_n = 0
    for i in range(2, tc//2+1):
        if li[i] == 0:
            if li[tc-i] == 0:
                s_n=i
                b_n=tc-i
                break
    print('%d = %d + %d' %((s_n+b_n),s_n, b_n))