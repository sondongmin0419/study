import sys
sys.setrecursionlimit(10**6)


cnt = 0


def sort_game(li, i):
    li_co = li[::]

    global cnt
    cnt += 1

    for j in range(K//2):
        li_co[i + j], li_co[i + K - j - 1] = li_co[i + K - j - 1], li_co[i + j]
        if li_co  == li_sort:
            return cnt

global N, K

N, K = map(int, input().split())

li = list(map(int, input().split()))
global li_sort
li_sort = li[::]
li_sort.sort()

result = {}

for i in range(N-K):
    sort_game(li, i)

print(cnt)


