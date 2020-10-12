def play(i):
    global r_c
    for r in range(10):
        for c in range(10):
            cnt = 0
            for a in range(i):
                for b in range(i):
                    if r+a > 9 or c+b > 9:
                        break
                    if li[r + a][c + b] == 1:
                        cnt += 1
                    else:
                        break
            if cnt == i * i:
                r_c += 1
                if li_[i - 1] > 0:
                    li_[i - 1] -= 1
                    for a in range(i):
                        for b in range(i):
                            li[r + a][c + b] = 0
                            
                else:
                    r_c = -1
                    return


li = [list(map(int, input().split())) for _ in range(10)]

li_ = [5, 5, 5, 5, 5]

i = 5
r_c = 0
for i in range(5,0,-1):
    play(i)

print(r_c)