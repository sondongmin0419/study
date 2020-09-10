import sys
sys.stdin = open("input_5176.txt", "r")


def root_num(index_):
    global root_n
    for i in range(2):
        if li[index_][i] != 0:
            root_n += 1
            root_num(li[index_][i])
    

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    N_2 = N//2
    stack = []
    li = [[0] * 2 for _ in range(N+1)]
    li_num = [0] * (N+1)
    n = 1
    index = 1
    while True:
        for i in range(2):
            if n < N:
                n += 1
                li[index][i] = n
        index += 1
        if n == N:
            break

    root_n = 1
    if li[1][0] != 0:
        index = 2
        root_n =2
        root_num(index)


    print(root_n)
