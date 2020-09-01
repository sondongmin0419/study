import sys
sys.stdin = open("input_4.txt", "r")


def game(p1_s, p2_s):
    if p1_s[1] == p2_s[1]:
        return p1_s
    elif p1_s[1] - p2_s[1] == -2 or p1_s[1] - p2_s[1] == 1:
        return p1_s
    elif p1_s[1] - p2_s[1] == -1 or p1_s[1] - p2_s[1] == 2:
        return p2_s


def play(li_test):
    if len(li_test) == 2:
        return game(li_test[0], li_test[1])
    if len(li_test) == 1:
        return li_test[0]
# 4 3  0 1 2 3  8 4 4
    li_1 = li_test[:(len(li_test)+1)//2]
    li_2 = li_test[(len(li_test)+1)//2:]
    p1 = play(li_1)
    p2 = play(li_2)
    return game(p1, p2)

    # if N % 2 == 0:  # 짝수
    #     for _ in range(N//2):
    #         p1 = stack.pop(0)
    #         p2 = stack.pop(0)
    #         stack.append(game(p1, p2))
    #     return
    # elif N % 2 == 1:  # 홀수
    #     for _ in range(N//2-1):
    #         p1 = stack.pop(0)
    #         p2 = stack.pop(0)
    #         stack.append(game(p1, p2))
    #     return


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    stack = []

    li = list(map(int, input().split()))
    li_li = [[0] for _ in range(N)]
    for i in range(N):
        li_li[i] = [i+1, li[i]]

    len_s = 0

    result = play(li_li)
    # while True:
    #     len_s = len(stack)
    #     play(len_s)
    #     if len(stack) == 1:
    #         break
    # result = stack.pop()

    print('#%d %d' % (TC, result[0]))
