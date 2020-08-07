T = int(input())

for TC in range(1, T+1):
    P, A, B = map(int, input().split())
    la = lb = 1
    ra = rb = P
    ca = cb = 0
    cnt_1 = 0
    cnt_2 = 0

    while True:
        cnt_1 += 1
        c = (la + ra) // 2
        if c == A:
            break
        elif c > A:
            ra = c
        else:
            la = c

    while True:
        cnt_2 += 1
        c = (lb + rb) // 2
        if c == B:
            break
        elif c > B:
            rb = c
        else:
            lb = c
    print(f'#{TC} ', end='')
    if cnt_1 > cnt_2:
        print('B')
    elif cnt_1 == cnt_2:
        print(0)
    else:
        print('A')
