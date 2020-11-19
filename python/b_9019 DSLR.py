def d1234(n):
    d4 = n % 10
    d3 = n // 10 % 10
    d2 = n // 100 % 10
    d1 = n // 1000
    return d1, d2, d3, d4


def D(n, al):
    if n * 2 >= 10000:
        if n*2/2 not in total:
            stack.append(n * 2 / 2)
            total.add(n * 2 / 2)
            stack_al.append((al+'D'))
        return
    else:
        if n*2 not in total:
            stack.append(n*2)
            total.add(n*2)
            stack_al.append((al+'D'))
        return


def S(n, al):
    if n - 1 >= 0:
        if n-1 not in total:
            stack.append(n-1)
            total.add(n-1)
            stack_al.append(al+'S')
        return
    else:
        if 9999 not in total:
            stack.append(9999)
            total.add(9999)
            stack_al.append(al+'S')
        return


def L(n, al):
    d1, d2, d3, d4 = d1234(n)
    n_n = d2 * 1000 + d3 * 100 + d4 * 10 + d1
    if n_n not in total:
        stack.append(n_n)
        total.add(n_n)
        stack_al.append(al + 'L')
    return


def R(n, al):
    d1, d2, d3, d4 = d1234(n)
    n_n = d4 * 1000 + d1 * 100 + d2 * 10 + d3
    if n_n not in total:
        stack.append(n_n)
        total.add(n_n)
        stack_al.append(al + 'R')
    return


T = int(input())

for TC in range(1, T + 1):
    A, B = map(int, input().split())
    stack = []
    stack_al = ['']
    total = set()
    stack.append(A)
    total.add(A)
    result_al = ''
    idx = -1
    
    while stack:
        s_l = len(stack)
        for _ in range(s_l):
            test_num = stack.pop(0)
            test_al = stack_al.pop(0)
            D(test_num, test_al)
            S(test_num, test_al)
            L(test_num, test_al)
            R(test_num, test_al)
            if B in stack:
                idx = stack.index(B)
                result_al = stack_al[idx]
                stack = []
                break

    print(result_al)
