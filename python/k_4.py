def solution(n, s, a, b, fares):
    li = [[0] * (n+1) for _ in range(n+1)]
    li_li = [0]*(n+1)
    visited = [0] * (n+1)
    stack = []

    def dfs_play(s):
        global total
        for i in range(n+1):
            if li_li[s][i] != 0 and visited[i] == 0:
                visited[i] = 1
                total += li_li[s][i]
                dfs_play(i)
                total -= li_li[s][i]
                visited[i] = 0
        return


    for i in range(fares):
        li[fares[i][0]][fares[i][1]] = fares[i][2]
        li[fares[i][1]][fares[i][2]] = fares[i][2]
    total = 0
    visited(s) = 1
    dfs_play(s)


    answer = 0

    return answer