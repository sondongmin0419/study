N, K = map(int, input().split())

li = list(map(str, input().split()))


stack = set()
li_sr = sorted(li)


v = []
v2 = []
v.append(li)
stack.add(''.join(li))
result = 0
cnt = 1
if li == li_sr:
    cnt = 0
while li != li_sr:
    if result == 1:
        break
    if len(v) == 0:
        cnt += 1
        v = v2[::]
        v2 = []
        if len(v) == 0:
            cnt = -1
            break

    test = v.pop(0)
    for i in range(len(test)-K+1):  # 0 ~ 7 K = 3 6 0 1 2 3 4 5
        test_a = test[::]
        for j in range(K//2):
            test_a[i+j], test_a[i+K-1-j] = test[i+K-1-j], test[i+j]
        if test_a == li_sr:
            result = 1
            break
        s = ''.join(test_a)
        if s not in stack:
            stack.add(s)
            v2.append(list(s))

print(cnt)