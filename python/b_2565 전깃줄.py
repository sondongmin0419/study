N = int(input())

arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

arr.sort(key=lambda x: (x[0], x[1]))
cnt = [1] * N
for i in range(1,N):
    cnti = 1

    for j in range(i):

        if arr[i][0] > arr[j][0] and arr[i][1] > arr[j][1]:
            if cnti < cnt[j]+1:
                cnti = cnt[j]+1
    cnt[i] = cnti
print(N-max(cnt))