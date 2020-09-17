# import time
# start = time.time()

def play(s_n):   # s_n 몇줄짜리인지
    global max_sum
    for p_n in range(1, N + 1):  # y 좌표
        if p_n + s_n > N+1:
            return
        for p_j in range(N - 1 - (p_n - 1), N - 1 + (p_n - 1) + 1):  # x좌표
            if p_n + p_j % 2 != N & 2:
                sum_sc = sum_score(s_n, p_n, p_j)
                if sum_sc > max_sum:
                    max_sum = sum_sc
            else:
                sum_sc = li_tr[p_n][p_j]
                if sum_sc > max_sum:
                    max_sum = sum_sc
            

def sum_score(sc_n, now_n, sc_j):
    sum = 0
    for n in range(now_n, now_n+sc_n):
        for j in range(sc_j-(n-now_n), sc_j+(n-now_n)+1):
            sum += li_tr[n][j]

    return sum


while True:
    li = list(map(int, input().split()))
    tc = 1

    N = li[0]
    if N == 0:
        break
    li_index = 1
    li_tr = [[0] * (2 * N - 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        for j in range(N - 1 - (n - 1), N - 1 + (n - 1) + 1):
            li_tr[n][j] = li[li_index]
            li_index += 1
    max_sum = 0

    for n in range(N, 0, -1):
        play(n)

    print(max_sum)
    tc += 1
# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간