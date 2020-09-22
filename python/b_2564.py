r, c = map(int, input().split())

store_num = int(input())


def play(nc, nr):
    global result
    global cnt

    for i in range(store_num):
        mc, mr = li[i]
        len_i = 0
        if nc == mc == 0 or nc == mc == c:
            len_i = abs(nr-mr)
        elif nr == mr == 0 or nr == mr == r:
            len_i = abs(nc-mc)
        elif (nc == 0 or nc == c) and (mc == 0 or mc == c):
            len_1 = nr+mr+nc+mc
            len_2 = (r-nr)+(r-mr)+nc+mc
            len_i = min(len_1, len_2)
        elif (nr == 0 or nr == r) and (mr == 0 or mr == r):
            len_1 = nr + mr + nc + mc
            len_2 = (c - nc) + (c - mc) + nr + mr
            len_i = min(len_1, len_2)
        else:
            len_i = abs(mr-nr) + abs(mc-nc)
        result += len_i
            # result += len_i
            # visited[i] = 1
            # cnt += 1
            # if result > min_result:
            #     return
            # if cnt == store_num:
            #     if min_result > result:
            #         min_result = result
            #         return
            # play(mc, mr)
            # visited[i] = 0
            # result -= len_i
            # cnt -= 1

li = [0] * (store_num+1)

for i in range(store_num+1):
    a, b = map(int, input().split())  # 1북 2남 3서 4동
    if a == 1:
        li[i] = [0, b]
    elif a == 2:
        li[i] = [c, b]
    elif a == 3:
        li[i] = [b, 0]
    else:
        li[i] = [b, r]
                         # 북남 왼쪽부터거리  동서 위쪽부터 거리
result = 0
cnt = 0
min_result = 400*400
d_xy = li.pop()
stack = []
visited = [0] * store_num
stack.append((b,r))
play(d_xy[0], d_xy[1])
print(result)