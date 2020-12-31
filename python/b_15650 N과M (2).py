N, M = map(int, input().split())

def b_15650(n):
    if len(li) == M:
        print(*li)
    if n>N:
        return
    for i in range(n,N+1):
        li.append(i)
        b_15650(i+1)
        li.pop()
    return

li = []
b_15650(1)