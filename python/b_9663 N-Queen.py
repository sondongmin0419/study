N = int(input())


def b_9663(y):
    global cnt
    if y == N:
        cnt += 1
        return
    for x in range(N):
        if li_x[x] == 0 and li_m[y - x + N] == 0 and li_p[y + x] == 0:
            li_m[y - x + N] = 1
            li_p[y + x] = 1
            li_x[x] = 1
            b_9663(y + 1)
            li_m[y - x + N] = 0
            li_p[y + x] = 0
            li_x[x] = 0


cnt = 0
n_N = N // 2
li_m = [0] * N * 2
li_p = [0] * N * 2
li_x = [0] * N
if N % 2 != 0:
    n_N += 1
for x in range(n_N):
    li_m[-x + N] = 1
    li_p[x] = 1
    li_x[x] = 1
    b_9663(1)
    li_m[-x + N] = 0
    li_p[x] = 0
    li_x[x] = 0
    if x == (N // 2) - 1:
        cnt *= 2
print(cnt)
