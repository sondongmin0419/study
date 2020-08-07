A, B, V = map(int, input().split())

cnt = 0

cnt_1 = (V-A)/(A-B) + 1
if cnt_1 > (V-A)//(A-B) + 1:
    cnt_1 += 1

print(int(cnt_1))
