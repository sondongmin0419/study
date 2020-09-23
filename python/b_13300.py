N, K = map(int, input().split())

li = [[0] * 2 for _ in range(7)]
for i in range(N):
    S, Y = map(int, input().split())
    li[Y][S] += 1

room_n = 0
for i in range(1,7):
    for j in range(2):
        if li[i][j] == 0:
            continue
        else:
            room_ij = 0
            while True:
                room_ij += 1
                if li[i][j] <= K * room_ij:
                    break
            room_n += room_ij

print(room_n)