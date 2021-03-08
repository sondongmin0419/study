E, EM, M, MH, H = map(int, input().split())

max_p = 0

e = E + EM # 쉬운문데
m = M  # 중간문제
h = H + MH  # 어려운문제

while True:
    min_v = min(e, m, h)
    if min_v == e:
        break
    elif min_v == h:
        break
    elif min_v == m:
        if e >= h:
            if e == E:
                if h == H:
                    break
                else:
                    h -= 1
                    m += 1
            else:
                e -= 1
                m += 1
        else:
            if h == H:
                if e == E:
                    break
                else:
                    e -= 1
                    m += 1
            else:
                    h -= 1
                    m += 1


print(min(e, m, h))
