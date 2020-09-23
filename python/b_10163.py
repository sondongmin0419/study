N = int(input())

li = [[-1]*101 for _ in range(101)]
li_n = [0] * N
for i in range(N):
    x, y, r, c = map(int, input().split())
    for col in range(y,y+c):
        for row in range(x, x+r):
            if li[col][row] == -1:
                li_n[i] += 1
                li[col][row] = i
            else:
                old_n = li[col][row]
                li_n[old_n] -= 1
                li_n[i] += 1
                li[col][row] = i
for i in range(N):
    print(li_n[i])