import math


def play_b():
    global cnt

    for i in range(int(s * C) + 1, math.ceil(e * C)-1):
        b = int(math.ceil(i * B / C) - math.ceil(s * B))
        d = int(math.ceil(e * D) - int(i * D / C))

        if b*d >0:
            cnt += b * d


B, C, D = map(int, input().split())
A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())

cnt = 0
s = A1 / A2
e = E1 / E2

play_b()
print(cnt)
