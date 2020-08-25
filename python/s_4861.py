import sys


def palindrome(li):
    if li == li[::-1]:
        return 1
    else:
        return 0


T = int(input())

for TC in range(1, T+1):
    result = ""
    N, M = map(int, sys.stdin.readline().split())
    li = [0] * N
    for i in range(N):
        s = sys.stdin.readline().strip()
        li[i] = list(s)
        for k in range(N-M+1):
            if palindrome(li[i][k:k+M]):
                result = s
    for k in range(N-M+1):
        for i in range(N):
            s_li = []
            for j in range(M):
                s_li.append(li[k+j][i])
            if palindrome(s_li):
               result = ''.join(s_li)
    print(f'#{TC} {result}')