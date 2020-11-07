# import sys
# sys.stdin = open("input_1.txt", "r")


def play(n):
    global total

    for j in range(N):
        if visited[j] == 0 and li_P[n][j] != 0:
            visited[j] = 1
            total *= li_P[n][j]
            if n == N-1:
                stack.append(total)
                visited[j] = 0
                total /= li_P[n][j]
                return
            play(n+1)
            visited[j] = 0
            total /= li_P[n][j]
    return


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    li_P = [list(map(int, input().split())) for _ in range(N)]
    stack = []
    visited = [0] * N
    total = 1
    play(0)
    print(max(stack))

