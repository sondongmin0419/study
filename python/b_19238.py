N, M, oil = map(int, input().split())

dr = [0, 1, 0, -1] # 상 우 하 좌
dc = [-1, 0, 1, 0]


def f_co(y, x):

    def play(y, x):
        for i in range(4):
            ny = y + dc[i]
            nx = x + dr[i]
            if 0 < ny <= N and 0 < nx <= N and li_map[ny][nx] != 1:
                if li_map[ny][nx] == 2:
                    stack_2.append((ny, nx))
                if (ny, nx) not in stack and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    stack.append((ny, nx))
                    visited.add((ny, nx))
        return

    global oil
    stack = []  # 이동좌표 스택
    stack_2 = []  # 고객만난좌표 스택
    stack.append((y, x))
    visited = set()
    visited.add((y, x))

    if (y, x) in dic_comstomer and li_map[y][x] == 2:
        li_map[y][x] = 0
        return (y, x)
    else:
        while True:
            oil -= 1
            if oil < 0:
                return
            else:
                len_stack = len(stack)
                for i in range(len_stack):
                    y, x = stack.pop(0)
                    play(y, x)
                if stack_2:

                    break
    stack_2.sort()
    costomer = stack_2[0]
    li_map[costomer[0]][costomer[1]] = 0
    return costomer


def f_(y, x, fy, fx):
    global oil
    global cnt
    cnt = 0


    def play(y, x):
        for i in range(4):
            ny = y + dc[i]
            nx = x + dr[i]
            if 0 < ny <= N and 0 < nx <= N and li_map[ny][nx] != 1:
                if (ny, nx) == (fy, fx):
                    stack_2.append((ny, nx))
                    return
                if (ny, nx) not in stack and (ny, nx) not in visited:
                    stack.append((ny, nx))
                    visited.add((ny, nx))
        return

    stack = []  # 이동좌표 스택
    stack_2 = []  #
    stack.append((y, x))
    visited = set()


    while True:
        visited.add((y, x))
        oil -= 1
        cnt += 1
        if oil < 0:
            return
        else:
            len_stack = len(stack)
            for i in range(len_stack):
                y, x = stack.pop(0)
                play(y, x)
            if stack_2:
                break

    f_area = stack_2[0]
    return f_area




li_map = [[0]*(N+1)]
for _ in range(N):
    li_map.append([0]+list(map(int, input().split())))  # 0 ~ N-1 인덱스

y, x = map(int, input().split())

li_costomer = []
dic_comstomer = {}
cnt = 0

for i in range(M):
    li_costomer.append(list(map(int, input().split())))
    li_map[li_costomer[i][0]][li_costomer[i][1]] = 2
    dic_comstomer[(li_costomer[i][0],li_costomer[i][1])] = (li_costomer[i][2],li_costomer[i][3])


for _ in range(M):

    costomer_yx = f_co(y, x)
    if oil < 0:
        break
    fy, fx = dic_comstomer[costomer_yx]
    f_area = f_(costomer_yx[0], costomer_yx[1], fy, fx)
    if oil >= 0:
        oil += cnt * 2
        y, x = f_area
    else:
        break

print(oil)
