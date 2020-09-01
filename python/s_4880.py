# import sys
# sys.stdin = open("input_4.txt", "r")


def game(p1_s, p2_s):
    if p1_s[1] == p2_s[1]:
        return p1_s
    elif p1_s[1] - p2_s[1] == -2 or p1_s[1] - p2_s[1] == 1:
        return p1_s
    elif p1_s[1] - p2_s[1] == -1 or p1_s[1] - p2_s[1] == 2:
        return p2_s


def play(N):
    if N % 2 == 0:  # 짝수
        for _ in range(N//2):
            p1 = stack.pop(0)
            p2 = stack.pop(0)
            stack.append(game(p1, p2))
        return
    elif N % 2 == 1:  # 홀수
        for _ in range(N//2-1):
            p1 = stack.pop(0)
            p2 = stack.pop(0)
            stack.append(game(p1, p2))
        return

#9개      9
#     5       4
#   3   2   2   2
#  2 1 1  1 1 1 1 1
# 1 1                    4회
T = int(input())

for TC in range(1, T+1):
    N = int(input())
    stack = []

    li = list(map(int, input().split()))
    li_li = [[0] for _ in range(N+1)]
    for i in range(N):
        stack.append([i+1, li[i]])

    len_s = 0
    if N % 2 == 1:
        p1 = stack.pop(0)
        p2 = stack.pop(0)
        p3 = game(p1, p2)
        p4 = stack.pop(0)
        stack.append(game(p3, p4))

    while True:
        len_s = len(stack)
        play(len_s)
        if len(stack) == 1:
            break
    result = stack.pop()

    print('#%d %d' % (TC, result[0]))


#     4 3
#   2 2 2 1
#1 1 1 1 1 1 1