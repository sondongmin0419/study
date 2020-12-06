import sys

N, M = map(int, sys.stdin.readline().strip().split())

li_n = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]
li_m = [str(sys.stdin.readline()) for _ in range(M)]
li_M = []
for i in range(len(li_m)):
    word = []
    stack = []
    for j in range(len(li_m[i])):
        if 65 <= ord(li_m[i][j]) <= 90:
            stack.append(li_m[i][j])
        else:
            stack_ = ''.join(stack[:])
            word.append([''.join(stack_)])
            stack = []
            word = []

    li_M.append([word])
print(li_m[0][0])

# 65 ~ 90
