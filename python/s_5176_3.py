T = int(input())


def play(v):
    if v*2 <= N:
        play(v*2)
        stack.append(v)
        if v*2+1 <= N:
            play(v*2 +1)
    else:
        stack.append(v)
    return


for TC in range(1, T+1):
    N = int(input())
    li = [0] * (N+1)
    stack = [0]
    play(1)
    print('#%d %d %d' % (TC, stack.index(1), stack.index(N//2)))