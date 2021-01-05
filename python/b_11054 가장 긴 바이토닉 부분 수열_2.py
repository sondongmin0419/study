N = int(input())

A = list(map(int, input().split()))
len_up = [1]*N
len_down = [1] * N


result_up = [A[0]]
result_down = [A[-1]]

for i in range(1, N):
    if result_up[-1] < A[i]:
        result_up.append(A[i])
    else:
        for j in range(len(result_up)):
            if result_up[j] >= A[i]:
                result_up[j] = A[i]
                break

    if result_down[0] < A[N-1-i]:
        result_down.insert(0,A[N-1-i])
    else:
        for j in range(len(result_down)-1,-1,-1):
            if result_down[j] >= A[i]:
                result_down[j] = A[i]
                break
    len_up[i] = len(result_up)
    len_down[N-1-i] = len(result_down)

result_ = 1

for i in range(N):
    total = len_up[i] + len_down[i] -1
    if total > result_:
        result_ = total
print(result_)

