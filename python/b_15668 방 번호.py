N = int(input())


def sol(n):
    n *= 10
    if n > 10 ** 5:
        n = n // 10
        return
    for i in range(10):
        if visited[i] == 0:
            n += li[i]
            if n == 0:
                continue
            visited[i] = 1
            li_result.append(n)
            sol(n)
            visited[i] = 0
            n -= li[i]

    n = n // 10
    return


li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
visited = [0] * 10
li_result = []
sol(0)

li_result.sort()

k = 1
for i in range(10):
    if N // 10 == 0:
        break

check = False

for B in li_result:
    li = [0] * 10
    A = N - B
    if A<=0:
        break

    A_ = str(A)
    B_ = str(B)
    for a in A_:
        li[int(a)] += 1
    for b in B_:
        li[int(b)] += 1
    cnt = 0
    for i in li:
        if i >1:
            cnt+=1
            break
    if cnt == 0:
        check = True
        print(A,' + ',B)
        break
if check:
    pass
else:
    print(-1)
