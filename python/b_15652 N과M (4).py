N, M = map(int, input().split())


def b_15651(n):
    if len(li) == M:
        print(*li)
        return
    if n > N:
        return
    for i in range(n, N + 1):
        li.append(i)
        b_15651(i)
        li.pop()
    return


li = []
b_15651(1)
