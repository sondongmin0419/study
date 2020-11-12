import math


def play_b():
    global cnt

    for c in range(int(s * C) + 1, math.ceil(e * C)):
        cnt_b = math.ceil(c * B / C) - (int(s * B) + 1)
        cnt_c = math.ceil(e * D) - (int(c * D / C) + 1)

        if cnt_b <= 0 or cnt_c <= 0:
            continue

        cnt += cnt_b * cnt_c


B, C, D = map(int, input().split())
A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())

cnt = 0
s = A1 / A2
e = E1 / E2
play_b()
print(cnt)

# print(int(4), int(4.6))
# print(math.ceil(4), math.ceil(4.6))
