import sys
sys.stdin = open("input.txt", "r")


def palindrome(li):
    if li == li[::-1]:
        return 1
    else:
        return 0


T = int(input())

for TC in range(1, T+1):
    result = ''
    N, M = map(int, input().split())
    li = [0] * N
    for i in range(N):
        s = input()
        li[i] = list(s)
        for k in range(N-M+1):
            if palindrome(li[i][k:k+M]):
                result = ''.join(li[i][k:k + M])
    if result == '':
        for k in range(N-M+1):
            for i in range(N):
                s_li = []
                for j in range(M):
                    s_li.append(li[k+j][i])
                if palindrome(s_li):
                   result = ''.join(s_li)
    print(f'#{TC} {result}')