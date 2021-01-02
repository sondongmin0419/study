T = int(input())

TC = [int(input()) for _ in range(T)]

max_TC = max(TC)

fibo_0 = [0] * (max_TC+1)
fibo_1 = [0] * (max_TC+1)

fibo_0[0] = 1
fibo_1[1] = 1

for i in range(2,max_TC+1):
    fibo_1[i] = fibo_1[i-1]+fibo_1[i-2]
    fibo_0[i] = fibo_0[i-1]+fibo_0[i-2]

for tc in TC:
    print(fibo_0[tc], fibo_1[tc])