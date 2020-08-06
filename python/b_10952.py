n = 1
while(n>0):
    a, b = map(int,input().split())
    n = a + b
    if n == 0:
        break
    print(n)