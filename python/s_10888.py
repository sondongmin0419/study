T = int(input())

def play(f_xy):
    dis = []
    for home_xy in li_home:
        dis.append(abs(home_xy[0]-f_xy[0]) + abs(home_xy[1]-f_xy[1]) + li[f_xy[0]][f_xy[1]])




for TC in range(1, T+1):
    N = int(input())

    li = [list(map(int, input().split())) for _ in range(N)]
    li_food = []
    li_home = []
    for i in range(N):
        for j in range(N):
            if li[i][j] > 1:
                li_food.append([i, j])
            elif li[i][j] == 1:
                li_home.append([i,j])


    for food_xy in li_food:
        play(food_xy)