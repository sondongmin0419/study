n = int(input())

def hanoi(n, A, B, C):
    if n == 1:
        print('%d %d' % (A, C))
        pass
    else:
        hanoi(n - 1, A, C, B)
        print('%d %d' % (A, C))
        hanoi(n - 1, B, A, C)


print(2**n-1)
hanoi(n, 1, 2, 3)
