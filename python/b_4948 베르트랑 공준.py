li_tc = []

while True:
    n = int(input())
    if n == 0:
        break
    li_tc.append(n)

max_tc = max(li_tc)

li = [1 for _ in range(max_tc*2)]
li[0] = 1

for i in range(2, max_tc+1):
    if li[i] == 1:
        for j in range(i * 2, max_tc*2, i):
            li[j] = 0

for tc in li_tc:
    print(sum(li[tc+1:tc*2+1]))