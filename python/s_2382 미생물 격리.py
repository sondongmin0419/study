d = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def play():
    for i in range(N):
        for j in range(N):
            for _ in range(len(li[i][j])):
                




    for i in range(K):
        li[i][0] += d[li[i][3]-1][0]
        li[i][1] += d[li[i][3]-1][1]
        li_[li[i][0]][li[i][1]].append([li[i][2], [li[i][3]]])
        if li[i][0] == 0 or li[i][0] == N-1:
            li[i][3] = li[i][3] % 2 + 1
            li[i][2] = li[i][2] // 2
        elif li[i][1] == 0 or li[i][1] == N-1:
            if li[i][3] == 3:
                li[i][3] = 4
            else:
                li[i][3] = 3
            li[i][2] = li[i][2] // 2

    return


T = int(input())

for TC in range(1, T + 1):
    N, M, K = map(int, input().split())

    li = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        t_li = list(map(int, input().split()))
        li[t_li[0]][t_li[1]].append([t_li[2], t_li[3]])
    print(li)
    for i in range(M):
        play()
    # result = 0
    # for i in range(K):
    #     result += li[i][2]
    # print(result)

