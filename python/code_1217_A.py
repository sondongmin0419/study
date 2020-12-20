T = int(input())

for TC in range(1, T + 1):
    a, b, c = map(int, input().split())
    k = (a+b+c)//9
    if a < k or b < k or c < k:
        print('NO')
    else:
        if (a+b+c) % 9 == 0:
            print('YES')
        else:
            print('NO')