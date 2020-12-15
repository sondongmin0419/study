import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for TC in range(1, T + 1):
    arr_p = list(input().rstrip())
    n = int(input())
    arr_n = input().rstrip()

    if len(arr_n) > 2:
        d_n = deque(map(int, arr_n.rstrip(']').lstrip('[').split(',')))
    else:
        d_n = deque([])
    check = True
    check_reverse = -1

    i = len(arr_p) - 1
    for p in arr_p:
        if p == 'R':
            check_reverse *= -1
        elif p == 'D':
            if d_n:
                if check_reverse == 1:
                    d_n.pop()
                else:
                    d_n.popleft()
            else:
                check = False
                break

    if check:
        if check_reverse == 1 and d_n:
            d_n.reverse()
            print(''.join(str(list(d_n)).split()))
        else:
            print(''.join(str(list(d_n)).split()))
    else:
        print('error')
