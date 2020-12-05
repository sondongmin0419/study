T = int(input())


def play_x():
    global result
    li_1 = [[0] * N for _ in range(N)]
    li_2 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(1, N):
            if li[i][j] == li[i][j - 1] + 1:  # 증가
                if 0 <= j - X:
                    for k in range(1, X + 1):
                        li_1[i][j - k] += 1
                else:
                    li_1[i][j] = 2
            elif li[i][j] == li[i][j - 1] - 1:  # 감소
                if j + X - 1 < N:
                    for k in range(X):
                        li_1[i][j + k] += 1
                else:
                    li_1[i][j] = 2
            elif abs(li[i][j]-li[i][j-1])> 1:
                li_1[i][j] = 2

            if li[j][i] == li[j - 1][i] + 1:  # 증가
                if 0 <= j - X:
                    for k in range(1, X + 1):
                        li_2[i][j - k] += 1
                else:
                    li_2[i][j] = 2
            elif li[j][i] == li[j - 1][i] - 1:  # 감소
                if j + X - 1 < N:
                    for k in range(X):
                        li_2[i][j + k] += 1
                else:
                    li_2[i][j] = 2
            elif abs(li[j][i]-li[j-1][i])> 1:
                li_2[i][j] = 2

    for i in range(N):
        if max(li_1[i]) <= 1:
            result += 1
        if max(li_2[i]) <= 1:
            result += 1

    return


def play_y():
    return


for TC in range(1, T + 1):
    N, X = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    play_x()
    print('#%d %d' %(TC,result))
