def play(n_16):
    if ord(n_16) < 65:
        n_16 = int(n_16)
    else:
        n_16 = ord(n_16) - 55
    k = 0
    stack = []
    for _ in range(4):
        stack.append(n_16 % 2)
        n_16 = n_16 // 2
    for _ in range(4):
        a = stack.pop()
        result.append(str(a))
T = int(input())

for TC in range(1, T+1):
    N, num = map(str, input().split())
    N = int(N)
    num = list(num)
    result = []
    for i in range(N):
        play(num[i])
    print('#%d %s' %(TC, ''.join(result)))
