import sys

def play():
    i = 0
    while i < len(li_M):
        check = True
        for j in range(1, len(li_M[i])):
            if li_M[i][j] not in dic_n:
                check = False
        if check:
            total = 0
            for k in range(1, len(li_M[i])):
                total += dic_n[li_M[i][k]] * int(li_N[i][k-1])
            if li_M[i][0] in dic_n:
                if dic_n[li_M[i][0]] > total:
                    dic_n[li_M[i][0]] = total
            else:
                dic_n[li_M[i][0]] = total
            li_M.pop(i)
            li_N.pop(i)
        else:
            i+=1
    return



N, M = map(int, sys.stdin.readline().strip().split())

li_n = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
li_m = [str(sys.stdin.readline()) for _ in range(M)]
li_M = []
li_N = []
dic_n = {}
for i in range(N):
    dic_n[li_n[i][0]] = int(li_n[i][1])
li_m.sort()

for i in range(len(li_m)):
    word = []
    N = []
    s = 0
    for j in range(len(li_m[i])):
        if 65 <= ord(li_m[i][j]) <= 90:
            pass
        elif 49 <= ord(li_m[i][j]) <= 57:
            N.append(li_m[i][j])
            s = j+1
        else:
            word.append(li_m[i][s:j])
    li_M.append(word)
    li_N.append(N)



for i in range(M+1):
    if not li_M:
        break
    play()

if 'LOVE' in dic_n:
    if dic_n['LOVE'] > 1000000000:
        print(1000000001)
    else:
        print(dic_n['LOVE'])
else:
    print(-1)
