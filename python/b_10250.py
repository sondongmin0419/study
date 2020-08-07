T = int(input())
for TC in range(1, T+1):

    H, W, N= map(int,input().split())
    na = N % H
    n = N // H + 1
    if na == 0:
        na = H
        n -= 1
    if n < 10:
        n = '0'+str(n)
    print(f'{na}{n}')
