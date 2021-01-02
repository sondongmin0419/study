n = int(input())

if n == 1:
    print(1)
else:
    fibo = [0] * (n+1)
    fibo[1] = 1
    for i in range(2,n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]

    print(fibo[n])
